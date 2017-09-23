from sklearn.neural_network import BernoulliRBM as _BernoulliRBM

from base import BaseAlgo
from base import TransformerMixin
from util.param_util import convert_params

class BernoulliRBM(TransformerMixin, BaseAlgo):
    def __init__(self, options):
        self.handle_options(options)

        params = options.get('params', {})

        out_params = convert_params(
            params,
            ints=['random_state', 'n_components', 'batch_size', 'n_iter'],
            floats=['learning_rate'],
            aliases={'k': 'n_components'},
            )

        self.estimator = _BernoulliRBM(**out_params)

    @staticmethod
    def register_codecs():
        from codec.codecs import SimpleObjectCodec
        from codec import codecs_manager
        codecs_manager.add_codec('examples.BernoulliRBM', 'BernoulliRBM', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.neural_network.rbm', 'BernoulliRBM', SimpleObjectCodec)
