import minerl
import gym
import threading
import argparse
import time



def main():
    """
    Runs a test which runs many instances of minerl simultaneously.
    """
    parser = argparse.ArgumentParser(description='The multi-environment stress test.')
    parser.add_argument("ninstances", help='Number of instances', type=int)

    opts = parser.parse_args()
    should_stop = False

    def run_instance():
        nonlocal should_stop
        try:
            env = gym.make('MineRLTreechop-v0')
            env.reset() 

            done = False
            while not (done or should_stop):
                env.step(env.action_space.sample())
        except:
            pass

    threads = [threading.Thread(target=run_instance) for _ in range(opts.ninstances)]

    for thread in threads:
        time.sleep(1) # Wait for  the thread to start.
        thread.start()

    time.sleep(20)
    should_stop = True


if __name__ == '__main__':
    main()