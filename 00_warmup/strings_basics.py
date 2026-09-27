from typing import Final

_A_LOWER: Final = ord("a")
_Z_LOWER: Final = ord("z")
_A_UPPER: Final = ord("A")
_Z_UPPER: Final = ord("Z")
_ALPHABET_SIZE: Final = 26


def caesar(text: str, shift: int) -> str:
    """Возвращает строку, зашифрованную шифром Цезаря.

    Символы вне латинского алфавита (кириллица, пунктуация, эмодзи)
    проходят без изменений. Сдвиг может быть любым целым числом,
    включая отрицательные.

    Args:
        text: Входная строка.
        shift: Величина сдвига в латинском алфавите. Любое целое число.

    Returns:
        Новая строка той же длины, что и ``text``.
    """
    norm_shift = shift % _ALPHABET_SIZE
    result: list[str] = []
    for char in text:
        code = ord(char)
        if _A_LOWER <= code <= _Z_LOWER:
            new_code = ((code - _A_LOWER + norm_shift) % _ALPHABET_SIZE) + _A_LOWER
            result.append(chr(new_code))
        elif _A_UPPER <= code <= _Z_UPPER:
            new_code = ((code - _A_UPPER + norm_shift) % _ALPHABET_SIZE) + _A_UPPER
            result.append(chr(new_code))
        else:
            result.append(char)
    return "".join(result)
