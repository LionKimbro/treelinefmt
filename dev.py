
import inject.args as args
import inject.inject as inject


def run():
    # args.mid_development()
    args.readargs()
    inject.run()


if __name__ == "__main__":
    run()

