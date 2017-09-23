from sklearn.ensemble import AdaBoostClassifier as _AdaBoostClassifier

from base import ClassifierMixin, BaseAlgo
from codec import codecs_manager
from util.param_util import convert_params

class AdaBoostClassifier(ClassifierMixin, BaseAlgo):
    def __init__(self, options):
        self.handle_options(options)

        params = options.get('params', {})

        converted_params = convert_params(
            params, 
            ints=['n_estimators'],
            floats=['learning_rate'])

        self.estimator = _AdaBoostClassifier(**converted_params)


    @staticmethod
    def register_codecs():
        from codec.codecs import SimpleObjectCodec, TreeCodec
        codecs_manager.add_codec('algos.AdaBoostClassifier', 'AdaBoostClassifier', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.ensemble.weight_boosting', 'AdaBoostClassifier', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.tree.tree', 'DecisionTreeClassifier', SimpleObjectCodec)
        codecs_manager.add_codec('sklearn.tree._tree', 'Tree', TreeCodec)
