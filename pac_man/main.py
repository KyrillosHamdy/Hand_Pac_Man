import raylib as rl
import cv2 as cv
import hand_tracking.hand_tracking_module as htm
from constants import *
from game import Game, draw_blocks, bfs, cell

def main():
    game = Game()

    cap = cv.VideoCapture(0)
    detector = htm.hand_detector(model_complexity=1, 
                                 min_detection_confidence=0.9)

    rl.InitWindow(COLS * TILE_SIZE, ROWS * TILE_SIZE, "pac".encode("utf-8"))
    rl.SetTargetFPS(60)

    game_over = False
    game_over_timer = 0.0

    counting_down = True
    countdown_timer = COUNTDOWN_DURATION

    while not rl.WindowShouldClose():
        success, frame = cap.read()
        frame = cv.flip(frame, 1)
        frame = detector.find_hands(frame)
        index_finger, hand_status = detector.find_position(frame)

        if counting_down:
            countdown_timer -= rl.GetFrameTime()
            if countdown_timer <= 0:
                counting_down = False
                game.player_elapsed = PLAYER_TIME_STEP
                game.monster_elapsed = MONSTER_TIME_STEP

        elif not game_over:
            game.player_elapsed += rl.GetFrameTime()
            game.monster_elapsed += rl.GetFrameTime()

            if game.player_elapsed >= PLAYER_TIME_STEP and index_finger and hand_status == [1, 1]:
                next_pos = cell(game.pac_man.x, game.pac_man.y)
                game.moved = False

                for lm in index_finger:
                    #left hand
                    if lm[3] == 0:
                        if lm[0] == 8: left_tip = lm[2]
                        if lm[0] == 6: left_pip = lm[2]

                    #right hand
                    if lm[3] == 1:
                        if lm[0] == 8: right_tip = lm[2]
                        if lm[0] == 6: right_pip = lm[2]

                # update x
                if left_tip < left_pip and right_tip > right_pip:
                    next_pos.x += 1; game.moved = True
                if left_tip > left_pip and right_tip < right_pip:
                    next_pos.x -= 1; game.moved = True

                # update y
                if left_tip < left_pip and right_tip < right_pip:
                    next_pos.y -= 1; game.moved = True
                if left_tip > left_pip and right_tip > right_pip:
                    next_pos.y += 1; game.moved = True

                if game.moved:
                    if game.is_valid_pos(next_pos) and game.player_elapsed >= PLAYER_TIME_STEP:
                        game.pac_man = next_pos
                        game.player_elapsed = 0
                    else:
                        game.player_elapsed = PLAYER_TIME_STEP

            if game.monster_elapsed >= MONSTER_TIME_STEP:
                monster_path = bfs(game.pac_man, game.monster)
                if len(monster_path) > 1:
                    game.monster = monster_path[1]
                    game.monster_elapsed = 0

            # Game over check
            if game.pac_man.x == game.monster.x and game.pac_man.y == game.monster.y:
                game_over = True
                game_over_timer = 0.0
        else:
            game_over_timer += rl.GetFrameTime()
            if game_over_timer >= GAME_OVER_DURATION:
                game.pac_man = cell(1, 1)
                game.monster = cell(10, 9)
                game_over = False
                counting_down = True
                countdown_timer = COUNTDOWN_DURATION

        rl.BeginDrawing()

        rl.ClearBackground(rl.WHITE)
        draw_blocks()

        rl.DrawCircleV(game.center_calc(game.pac_man), TILE_SIZE // 2, rl.YELLOW)
        rl.DrawCircleV(game.center_calc(game.monster), TILE_SIZE // 2, rl.RED)

        if counting_down:
            count_text = str(int(countdown_timer) + 1).encode("utf-8")
            font_size = 100
            text_width = rl.MeasureText(count_text, font_size)
            x = (COLS * TILE_SIZE - text_width) // 2
            y = (ROWS * TILE_SIZE - font_size) // 2
            rl.DrawText(count_text, x, y, font_size, rl.RED)

        if game_over:
            font_size = 90
            text_width = rl.MeasureText(GAME_OVER_TEXT, font_size)
            x = (COLS * TILE_SIZE - text_width) // 2
            y = (ROWS * TILE_SIZE - font_size) // 2
            rl.DrawText(GAME_OVER_TEXT, x, y, font_size, rl.WHITE)

        rl.EndDrawing()
        cv.imshow("Img", frame)
        cv.waitKey(1)

    rl.CloseWindow()
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()