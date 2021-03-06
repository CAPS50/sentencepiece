# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sentencepiece
else:
    import _sentencepiece

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


EncoderVersion_kOptimized = _sentencepiece.EncoderVersion_kOptimized
EncoderVersion_kOriginal = _sentencepiece.EncoderVersion_kOriginal
class SentencePieceProcessor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _sentencepiece.SentencePieceProcessor_swiginit(self, _sentencepiece.new_SentencePieceProcessor())
    __swig_destroy__ = _sentencepiece.delete_SentencePieceProcessor

    def Load(self, filename):
        return _sentencepiece.SentencePieceProcessor_Load(self, filename)

    def LoadOrDie(self, filename):
        return _sentencepiece.SentencePieceProcessor_LoadOrDie(self, filename)

    def LoadFromSerializedProto(self, serialized):
        return _sentencepiece.SentencePieceProcessor_LoadFromSerializedProto(self, serialized)

    def SetEncodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetEncodeExtraOptions(self, extra_option)

    def SetDecodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetDecodeExtraOptions(self, extra_option)

    def SetVocabulary(self, valid_vocab):
        return _sentencepiece.SentencePieceProcessor_SetVocabulary(self, valid_vocab)

    def ResetVocabulary(self):
        return _sentencepiece.SentencePieceProcessor_ResetVocabulary(self)

    def LoadVocabulary(self, filename, threshold):
        return _sentencepiece.SentencePieceProcessor_LoadVocabulary(self, filename, threshold)

    def SetEncoderVersion(self, encoder_version):
        return _sentencepiece.SentencePieceProcessor_SetEncoderVersion(self, encoder_version)

    def GetEncoderVersion(self):
        return _sentencepiece.SentencePieceProcessor_GetEncoderVersion(self)

    def EncodeAsPieces(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsPieces(self, input)

    def EncodeAsIds(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsIds(self, input)

    def NBestEncodeAsPieces(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsPieces(self, input, nbest_size)

    def NBestEncodeAsIds(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsIds(self, input, nbest_size)

    def SampleEncodeAsPieces(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsPieces(self, input, nbest_size, alpha)

    def SampleEncodeAsIds(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsIds(self, input, nbest_size, alpha)

    def DecodePieces(self, pieces):
        return _sentencepiece.SentencePieceProcessor_DecodePieces(self, pieces)

    def DecodeIds(self, ids):
        return _sentencepiece.SentencePieceProcessor_DecodeIds(self, ids)

    def EncodeAsSerializedProto(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsSerializedProto(self, input)

    def SampleEncodeAsSerializedProto(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsSerializedProto(self, input, nbest_size, alpha)

    def NBestEncodeAsSerializedProto(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsSerializedProto(self, input, nbest_size)

    def DecodePiecesAsSerializedProto(self, pieces):
        return _sentencepiece.SentencePieceProcessor_DecodePiecesAsSerializedProto(self, pieces)

    def DecodeIdsAsSerializedProto(self, ids):
        return _sentencepiece.SentencePieceProcessor_DecodeIdsAsSerializedProto(self, ids)

    def GetPieceSize(self):
        return _sentencepiece.SentencePieceProcessor_GetPieceSize(self)

    def PieceToId(self, piece):
        return _sentencepiece.SentencePieceProcessor_PieceToId(self, piece)

    def IdToPiece(self, id):
        return _sentencepiece.SentencePieceProcessor_IdToPiece(self, id)

    def GetScore(self, id):
        return _sentencepiece.SentencePieceProcessor_GetScore(self, id)

    def IsUnknown(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnknown(self, id)

    def IsControl(self, id):
        return _sentencepiece.SentencePieceProcessor_IsControl(self, id)

    def IsUnused(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnused(self, id)

    def IsByte(self, id):
        return _sentencepiece.SentencePieceProcessor_IsByte(self, id)

    def unk_id(self):
        return _sentencepiece.SentencePieceProcessor_unk_id(self)

    def bos_id(self):
        return _sentencepiece.SentencePieceProcessor_bos_id(self)

    def eos_id(self):
        return _sentencepiece.SentencePieceProcessor_eos_id(self)

    def pad_id(self):
        return _sentencepiece.SentencePieceProcessor_pad_id(self)

    def load(self, filename):
        return _sentencepiece.SentencePieceProcessor_load(self, filename)

    def load_from_serialized_proto(self, filename):
        return _sentencepiece.SentencePieceProcessor_load_from_serialized_proto(self, filename)

    def set_encode_extra_options(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_set_encode_extra_options(self, extra_option)

    def set_decode_extra_options(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_set_decode_extra_options(self, extra_option)

    def set_vocabulary(self, valid_vocab):
        return _sentencepiece.SentencePieceProcessor_set_vocabulary(self, valid_vocab)

    def reset_vocabulary(self):
        return _sentencepiece.SentencePieceProcessor_reset_vocabulary(self)

    def load_vocabulary(self, filename, threshold):
        return _sentencepiece.SentencePieceProcessor_load_vocabulary(self, filename, threshold)

    def encode_as_pieces(self, input):
        return _sentencepiece.SentencePieceProcessor_encode_as_pieces(self, input)

    def encode_as_ids(self, input):
        return _sentencepiece.SentencePieceProcessor_encode_as_ids(self, input)

    def nbest_encode_as_pieces(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_nbest_encode_as_pieces(self, input, nbest_size)

    def nbest_encode_as_ids(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_nbest_encode_as_ids(self, input, nbest_size)

    def sample_encode_as_pieces(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_sample_encode_as_pieces(self, input, nbest_size, alpha)

    def sample_encode_as_ids(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_sample_encode_as_ids(self, input, nbest_size, alpha)

    def decode_pieces(self, input):
        return _sentencepiece.SentencePieceProcessor_decode_pieces(self, input)

    def decode_ids(self, input):
        return _sentencepiece.SentencePieceProcessor_decode_ids(self, input)

    def encode_as_serialized_proto(self, input):
        return _sentencepiece.SentencePieceProcessor_encode_as_serialized_proto(self, input)

    def sample_encode_as_serialized_proto(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_sample_encode_as_serialized_proto(self, input, nbest_size, alpha)

    def nbest_encode_as_serialized_proto(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_nbest_encode_as_serialized_proto(self, input, nbest_size)

    def decode_pieces_as_serialized_proto(self, pieces):
        return _sentencepiece.SentencePieceProcessor_decode_pieces_as_serialized_proto(self, pieces)

    def decode_ids_as_serialized_proto(self, ids):
        return _sentencepiece.SentencePieceProcessor_decode_ids_as_serialized_proto(self, ids)

    def get_piece_size(self):
        return _sentencepiece.SentencePieceProcessor_get_piece_size(self)

    def piece_to_id(self, piece):
        return _sentencepiece.SentencePieceProcessor_piece_to_id(self, piece)

    def id_to_piece(self, id):
        return _sentencepiece.SentencePieceProcessor_id_to_piece(self, id)

    def get_score(self, id):
        return _sentencepiece.SentencePieceProcessor_get_score(self, id)

    def is_unknown(self, id):
        return _sentencepiece.SentencePieceProcessor_is_unknown(self, id)

    def is_control(self, id):
        return _sentencepiece.SentencePieceProcessor_is_control(self, id)

    def is_unused(self, id):
        return _sentencepiece.SentencePieceProcessor_is_unused(self, id)

    def __len__(self):
        return _sentencepiece.SentencePieceProcessor___len__(self)

    def __getitem__(self, key):
        return _sentencepiece.SentencePieceProcessor___getitem__(self, key)

# Register SentencePieceProcessor in _sentencepiece:
_sentencepiece.SentencePieceProcessor_swigregister(SentencePieceProcessor)

class SentenceIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _sentencepiece.delete_SentenceIterator

    def done(self):
        return _sentencepiece.SentenceIterator_done(self)

    def Next(self):
        return _sentencepiece.SentenceIterator_Next(self)

    def value(self):
        return _sentencepiece.SentenceIterator_value(self)

    def status(self):
        return _sentencepiece.SentenceIterator_status(self)

# Register SentenceIterator in _sentencepiece:
_sentencepiece.SentenceIterator_swigregister(SentenceIterator)

class SentencePieceTrainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    @staticmethod
    def Train(*args):
        return _sentencepiece.SentencePieceTrainer_Train(*args)

    @staticmethod
    def SetPretokenizerForTraining(pretokenizer):
        return _sentencepiece.SentencePieceTrainer_SetPretokenizerForTraining(pretokenizer)

    @staticmethod
    def GetPretokenizerForTraining():
        return _sentencepiece.SentencePieceTrainer_GetPretokenizerForTraining()

    @staticmethod
    def PopulateModelTypeFromString(type, trainer_spec):
        return _sentencepiece.SentencePieceTrainer_PopulateModelTypeFromString(type, trainer_spec)

    @staticmethod
    def train(args):
        return _sentencepiece.SentencePieceTrainer_train(args)

# Register SentencePieceTrainer in _sentencepiece:
_sentencepiece.SentencePieceTrainer_swigregister(SentencePieceTrainer)

def SentencePieceTrainer_Train(*args):
    return _sentencepiece.SentencePieceTrainer_Train(*args)

def SentencePieceTrainer_SetPretokenizerForTraining(pretokenizer):
    return _sentencepiece.SentencePieceTrainer_SetPretokenizerForTraining(pretokenizer)

def SentencePieceTrainer_GetPretokenizerForTraining():
    return _sentencepiece.SentencePieceTrainer_GetPretokenizerForTraining()

def SentencePieceTrainer_PopulateModelTypeFromString(type, trainer_spec):
    return _sentencepiece.SentencePieceTrainer_PopulateModelTypeFromString(type, trainer_spec)

def SentencePieceTrainer_train(args):
    return _sentencepiece.SentencePieceTrainer_train(args)



