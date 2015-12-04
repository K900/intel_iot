spark_chars = "_.-#"


def sparkify(series):
    series = [float(i) for i in series]
    minimum = min(series)
    maximum = max(series)
    data_range = maximum - minimum
    if data_range == 0.0:
        # Graph a baseline if every input value is equal.
        return ''.join([spark_chars[0] for _ in series])
    coefficient = (len(spark_chars) - 1.0) / data_range
    return ''.join([spark_chars[
                    int(round((x - minimum) * coefficient))] for x in series])


# noinspection PyUnusedLocal
# These variables are later made available to the debug IPython shell (implicitly). We want to keep them around.
def main():
    import logging
    import intel_iot.board.edison.arduino
    import intel_iot.util.gpio

    b = intel_iot.board.edison.arduino.board
    g = intel_iot.util.gpio

    logging.basicConfig(level=logging.DEBUG)

    import collections

    # noinspection PyUnusedLocal
    def graph_pin(p, n=80):
        d = collections.deque(maxlen=n)
        while True:
            d.append(p.value)
            print(sparkify(d), end='\r')

    # noinspection PyPackageRequirements
    # noinspection PyUnresolvedReferences
    # The debug shell is completely optional, and PyCharm doesn't understand the concept of optional dependencies.
    # However, this _will_ fail to run if IPython is not installed.
    import IPython

    IPython.embed()


if __name__ == "__main__":
    main()
