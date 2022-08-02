import pytest
from project import get_ayah_text, get_ayah_audio,shiekh_name_translator

def test_get_ayah_text():
    assert get_ayah_text(2,1) == ' الٓمٓ'
    assert get_ayah_text(36,1) ==  ' يسٓ'
    with pytest.raises(IndexError):
        get_ayah_text(1,500)

def test_get_ayah_audio():
    assert get_ayah_audio(2,1,"ar.husary") == "https://cdn.islamic.network/quran/audio/128/ar.husary/8.mp3"
    assert get_ayah_audio(114,1,"ar.abdulsamad") == "https://cdn.islamic.network/quran/audio/64/ar.abdulsamad/6231.mp3"
    with pytest.raises(TypeError):
        get_ayah_audio(1,500,"ar.abdulsamad")

def test_shiekh_name_translator():
    assert shiekh_name_translator("الحصري") == "ar.husary"
    assert shiekh_name_translator("السديس") == "ar.abdurrahmaansudais"

    