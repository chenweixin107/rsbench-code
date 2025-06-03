from rssgen.generators.mnist_generator import SyntheticMNISTGenerator

import pdb

class MNISTUtils(SyntheticMNISTGenerator):
    """Mnist Utils"""

    def __init__(
        self,
        mnist_path="/home/jovyan/workspace/datasets/MNIST/raw",
    ):
        super(MNISTUtils, self).__init__(
            output_path="",
            val_prop=0,
            test_prop=0,
            num_digits=1,
            digit_values=[0, 1],
            logic=None,
            symbols=None,
            multiple_labels=False,
            ood_prop=0,
            digit_len=1, ## New: accommodate to new MNMath settings
            mnist_path=mnist_path,
        )
