from pettingzoo.classic import chess_v6
from ..state import game_state


def run_sim(state="rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"):
    env = chess_v6.env(render_mode="human")
    env.reset()

    # Not actually used yet
    gameState = game_state.GameState(
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            action = None
        else:
            mask = observation["action_mask"]

            # Insert policy here

            action = env.action_space(agent).sample(mask)

        env.step(action)
        env.render()

    env.close()


run_sim()
