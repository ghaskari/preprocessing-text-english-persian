# Maps different numeric representations, including Arabic numerals and Persian/Urdu numerals, to standard Arabic digits (0-9).
num_dict = {
    '۹': '9',  # Maps Persian/Urdu digit for 9 to '9'
    '٩': '9',  # Maps Arabic digit for 9 to '9'
    '9': '9',  # Maps standard digit 9 to itself
    '۸': '8',  # Maps Persian/Urdu digit for 8 to '8'
    '٨': '8',  # Maps Arabic digit for 8 to '8'
    '8': '8',  # Maps standard digit 8 to itself
    '۷': '7',  # Maps Persian/Urdu digit for 7 to '7'
    '٧': '7',  # Maps Arabic digit for 7 to '7'
    '7': '7',  # Maps standard digit 7 to itself
    '۶': '6',  # Maps Persian/Urdu digit for 6 to '6'
    '٦': '6',  # Maps Arabic digit for 6 to '6'
    '6': '6',  # Maps standard digit 6 to itself
    '۵': '5',  # Maps Persian/Urdu digit for 5 to '5'
    '٥': '5',  # Maps Arabic digit for 5 to '5'
    '5': '5',  # Maps standard digit 5 to itself
    '۴': '4',  # Maps Persian/Urdu digit for 4 to '4'
    '٤': '4',  # Maps Arabic digit for 4 to '4'
    '4': '4',  # Maps standard digit 4 to itself
    '۳': '3',  # Maps Persian/Urdu digit for 3 to '3'
    '٣': '3',  # Maps Arabic digit for 3 to '3'
    '3': '3',  # Maps standard digit 3 to itself
    '۲': '2',  # Maps Persian/Urdu digit for 2 to '2'
    '٢': '2',  # Maps Arabic digit for 2 to '2'
    '2': '2',  # Maps standard digit 2 to itself
    '۱': '1',  # Maps Persian/Urdu digit for 1 to '1'
    '١': '1',  # Maps Arabic digit for 1 to '1'
    '1': '1',  # Maps standard digit 1 to itself
    '۰': '0',  # Maps Persian/Urdu digit for 0 to '0'
    '٠': '0',  # Maps Arabic digit for 0 to '0'
    '0': '0'   # Maps standard digit 0 to itself
}

# Converts various Arabic script characters to a standard form, particularly focusing on characters with multiple forms or dialectical variations.
arabic_dict = {
    'ك': 'ک',  # Maps Arabic form of 'kaf' to Persian/Urdu form 'ک'
    'ڪ': 'ک',  # Maps another form of 'kaf' to 'ک'
    'ک': 'ک',  # Maps Persian/Urdu 'kaf' to itself
    'ئ': 'ی',  # Maps Arabic 'ye' with hamza to Persian/Urdu 'ی'
    'ی': 'ی',  # Maps Persian/Urdu 'ye' to itself
    'ێ': 'ی',  # Maps Kurdish 'ye' to Persian/Urdu 'ی'
    'ي': 'ی',  # Maps Arabic 'ye' to Persian/Urdu 'ی'
    'ى': 'ی',  # Maps Arabic 'alif maqsura' to Persian/Urdu 'ی'
    'ۆ': 'و',  # Maps Kurdish 'waw' to Arabic/Persian 'و'
    'ؤ': 'و',  # Maps Arabic 'waw' with hamza to 'و'
    'و': 'و',  # Maps Arabic/Persian 'waw' to itself
    'ڕ': 'ر',  # Maps Kurdish 're' to Arabic/Persian 'ر'
    'ر': 'ر',  # Maps Arabic/Persian 're' to itself
    'ة': 'ه',  # Maps Arabic 'ta marbuta' to Persian 'ه'
    'ه': 'ه',  # Maps Arabic/Persian 'he' to itself
    'ہ': 'ه',  # Maps Urdu 'he' to Persian 'ه'
    'آ': ' ا',  # Maps Arabic 'alif with madda' to standard 'ا'
    'أ': 'ا',  # Maps Arabic 'alif with hamza above' to standard 'ا'
    'إ': 'ا',  # Maps Arabic 'alif with hamza below' to standard 'ا'
    # 'ا': 'ا',  # Maps Arabic/Persian 'alif' to itself
    'ء': 'ا',  # Maps Arabic hamza to 'ا'
    'ً': ' ',  # Removes Arabic tanween (fathatain)
    'ٌ': ' ',  # Removes Arabic tanween (dammatain)
    'ٍ': ' ',  # Removes Arabic tanween (kasratain)
    'َ': ' ',  # Removes Arabic fatha
    'ُ': ' ',  # Removes Arabic damma
    'ِ': ' ',  # Removes Arabic kasra
    'ﻴ': 'ی',  # Maps Arabic letter 'ye' final form to Persian/Urdu 'ی'
    'ﺗ': 'ت',  # Maps Arabic letter 'te' to standard form 'ت'
    'ﺮ': 'ر',  # Maps Arabic letter 're' final form to standard 'ر'
    'ﺤ': 'ح',  # Maps Arabic letter 'he' to standard form 'ح'
    'ﻧ': 'ن',  # Maps Arabic letter 'noon' to standard form 'ن'
    'ﺲ': 'س',  # Maps Arabic letter 'seen' to standard form 'س'
    'ﭘ': 'پ',  # Maps Persian letter 'pe' to standard form 'پ'
    'ﺪ': 'د',  # Maps Arabic letter 'dal' to standard form 'د'
    'ﺷ': 'ش',  # Maps Arabic letter 'sheen' to standard form 'ش'
    'ﻣ': 'م',  # Maps Arabic letter 'meem' to standard form 'م'
    'ﻮ': 'و',  # Maps Arabic letter 'waw' final form to standard 'و'
    'ﮔ': 'گ',  # Maps Persian letter 'gaf' to standard form 'گ'
    'ﻓ': 'ف',  # Maps Arabic letter 'fe' to standard form 'ف'
    'ﻗ': 'ق',  # Maps Arabic letter 'qaf' to standard form 'ق'
    'ﻦ': 'ن',  # Maps Arabic letter 'noon' final form to standard 'ن'
    'ﭐ': 'ا',  # Maps Arabic 'alif with hamza above isolated form' to standard 'ا'
    'ﺳ': 'س',  # Maps Arabic letter 'seen' initial form to standard 'س'
    'ۀ': 'ه',  # Maps Persian 'he with hamza above' to standard 'ه'
}

# Maps various punctuation marks, symbols, and some special characters in English text to standardized forms, spaces, or removes them entirely.
sign_dict_en = {
    ".": ' ',
    ":": ' ',
    '(': ' ',  # Maps left parenthesis to space
    ')': ' ',  # Maps right parenthesis to space
    '...': ' ',  # Maps ellipsis to a single period surrounded by spaces
    '..': ' ',  # Maps double period to a single period surrounded by spaces
    '. . .': ' ',  # Maps spaced ellipsis to a single period surrounded by spaces
    '…': ' ',  # Maps ellipsis symbol to a single period surrounded by spaces
    '"': ' ',  # Maps double quotation mark to itself
    '“': ' ',  # Maps left double quotation mark to standard double quote
    '”': ' ',  # Maps right double quotation mark to standard double quote
    '‘': ' ',  # Maps left single quotation mark to standard double quote
    '’': ' ',  # Maps right single quotation mark to standard double quote
    '""': ' ',  # Maps double double-quote to a single double quote
    # '-': ' ',  # Maps hyphen to hyphen surrounded by spaces
    '—': ' ',  # Maps em dash to space
    '_': ' ',  # Maps underscore to space
    '%': ' ',  # Maps percent sign to space
    '@': ' ',  # Removes at symbol
    '#': ' ',  # Removes hashtag
    '$': ' ',  # Removes dollar sign
    '^': ' ',  # Removes caret
    '&': ' ',  # Removes ampersand
    '*': ' ',  # Removes asterisk
    '{': ' ',  # Removes left curly brace
    '}': ' ',  # Removes right curly brace
    '?': ' ',  # Maps question mark to question mark surrounded by spaces
    '!': ' ',  # Maps exclamation mark to exclamation mark surrounded by spaces
    r'\\': '',  # Removes backslash
    '`': '',  # Removes backtick
    '|': '',  # Removes pipe symbol
    # '/': '',  # Removes forward slash
    '•': ' ',  # Maps bullet point to space
    '。': ' ',  # Maps Chinese period to space
    '¡': ' ',  # Maps inverted exclamation mark to space
    '¿': ' ',  # Maps inverted question mark to space
    '¨': ' ',  # Maps diaeresis to space
    '¯': ' ',  # Maps macron to space
    '°': ' ',  # Maps degree sign to space
    '±': ' ',  # Maps plus-minus sign to space
    '²': ' ',  # Maps squared sign to space
    '³': ' ',  # Maps cubed sign to space
    '´': ' ',  # Maps acute accent to space
    'µ': ' ',  # Maps micro sign to space
    '¶': ' ',  # Maps paragraph sign to space
    '·': ' ',  # Maps middle dot to space
    '¸': ' ',  # Maps cedilla to space
    '¹': ' ',  # Maps superscript one to space
    '☑': ' ',  # Maps ballot box with check to space
    '↓': ' ',  # Maps downwards arrow to space
    '➡': ' ',  # Maps rightwards arrow to space
    '⬅': ' ',  # Maps leftwards arrow to space
    '▫': ' ',  # Maps white small square to space
    '⃣': ' ',  # Maps keycap to space
    '»': ' ',  # Maps right double angle quote to standard double quote
    '«': ' ',  # Maps left double angle quote to standard double quote
    '<': ' ',  # Maps less-than sign to space
    '>': ' ',  # Maps greater-than sign to space
    '+': ' ',  # Maps plus sign to space
    '~': ' ',  # Maps tilde to space
    '=': ' ',  # Maps equals sign to space
    '×': ' ',  # Maps multiplication sign to space
    '《': ' ',  # Maps Chinese left double angle quote to space
    '》': ' ',  # Maps Chinese right double angle quote to space
    '「': ' ',  # Maps Chinese left corner bracket to space
    '」': ' ',  # Maps Chinese right corner bracket to space
    '、': ' ',  # Maps Chinese comma to space
    '｀': ' ',  # Maps Japanese full-width grave accent to space
    'ً': ' ',  # Maps Arabic fathatain to space
    '〜': ' ',  # Maps Japanese wave dash to space
    'ヽ': ' ',  # Maps Japanese iteration mark to space
    r'\n': ' ',  # Maps newline character to space
    r'\t': ' ',  # Maps tab character to space
    r'\r': ' ',  # Maps carriage return character to space
    ',': ' ',  # Maps comma to space
    '£': ' ',  # Maps pound sign to space
    '¢': ' ',  # Maps cent sign to space
    '€': ' ',  # Maps euro sign to space
    '\\': ' ',  # Maps single backslash to space
}

# Similar to sign_dict_en, but for Persian text; maps Persian punctuation marks and symbols to standardized forms or spaces.
sign_dict_fa_phase_one = {
    '%d': ' ',
    '%s': ' ',
    r"\u200c": " ",
    ',': ' ، ',  # Maps comma to Persian comma
    ';': ' ؛ ',  # Maps semicolon to Persian semicolon
    '؛': ' ؛ ',  # Maps Persian semicolon to space
    '?': ' ؟ ',  # Maps question mark to Persian question mark
    '؟': ' ؟ ',  # Maps Persian question mark to space
    '!': ' ! ',  # Maps exclamation mark to space
    '$': ' $ ',  # Removes dollar sign
    '%': ' ٪ ',  # Maps percent sign to space
    '٪': ' ٪ ',  # Maps Persian percent sign to space
    ':': ' : ',  # Maps colon to space
    '...': ' ',  # Maps ellipsis to a single period surrounded by spaces
    '..': ' ',  # Maps double period to a single period surrounded by spaces
    '. . .': ' ',  # Maps spaced ellipsis to a single period surrounded by spaces
    '.': ' . ',
    '…': ' ',  # Maps ellipsis symbol to a single period surrounded by spaces
    '،': ' ، ',
    # '-': ' ',  # Maps hyphen to space
    '—': ' ',  # Maps em dash to space
    '_': ' ',  # Maps underscore to space
    '@': '',  # Removes at symbol
    '#': '',  # Removes hashtag
    '^': '',  # Removes caret
    '&': '',  # Removes ampersand
    '*': '',  # Removes asterisk
    '{': '',  # Removes left curly brace
    '}': '',  # Removes right curly brace
    r'\\': '',  # Removes backslash
    '`': '',  # Removes backtick
    '|': '',  # Removes pipe symbol
    '•': ' ',  # Maps bullet point to space
    '。': ' ',  # Maps Chinese period to space
    '¡': ' ',  # Maps inverted exclamation mark to space
    '¿': ' ',  # Maps inverted question mark to space
    '¨': ' ',  # Maps diaeresis to space
    '¯': ' ',  # Maps macron to space
    '°': ' ',  # Maps degree sign to space
    '±': ' ',  # Maps plus-minus sign to space
    '²': ' ',  # Maps squared sign to space
    '³': ' ',  # Maps cubed sign to space
    '´': ' ',  # Maps acute accent to space
    'µ': ' ',  # Maps micro sign to space
    '¶': ' ',  # Maps paragraph sign to space
    '·': ' ',  # Maps middle dot to space
    '¸': ' ',  # Maps cedilla to space
    '¹': ' ',  # Maps superscript one to space
    '☑': ' ',  # Maps ballot box with check to space
    '↓': ' ',  # Maps downwards arrow to space
    '➡': ' ',  # Maps rightwards arrow to space
    '⬅': ' ',  # Maps leftwards arrow to space
    '▫': ' ',  # Maps white small square to space
    '⃣': ' ',  # Maps keycap to space
    '<': ' ',  # Maps less-than sign to space
    '>': ' ',  # Maps greater-than sign to space
    '+': ' ',  # Maps plus sign to space
    '~': ' ',  # Maps tilde to space
    '=': ' ',  # Maps equals sign to space
    '×': ' ',  # Maps multiplication sign to space
    '《': ' ',  # Maps Chinese left double angle quote to space
    '》': ' ',  # Maps Chinese right double angle quote to space
    'ٔ': ' ',  # Maps Arabic mark to space
    '「': ' ',  # Maps Chinese left corner bracket to space
    '」': ' ',  # Maps Chinese right corner bracket to space
    '、': ' ',  # Maps Chinese comma to space
    '｀': ' ',  # Maps Japanese full-width grave accent to space
    '〜': ' ',  # Maps Japanese wave dash to space
    'ヽ': ' ',  # Maps Japanese iteration mark to space
    r'\n': ' ',  # Maps newline character to space
    r'\r': ' ',  # Maps carriage return character to space
    r'\t': ' ',  # Maps tab character to space
    '\\': ' ',  # Maps single backslash to space
    '‎': ' ',  # Maps left-to-right mark to space
    r'\u00A0': ' ',  # Maps non-breaking space to space
    '–': ' ',  # Maps en dash to space
    'ّ': '',  # Removes Arabic shadda
    'َ': '',  # Removes Arabic fatha
    'ُ': '',  # Removes Arabic damma
    'ِ': '',  # Removes Arabic kasra
    'ٌ': '',  # Removes Arabic dammatain
    'ٍ': '',  # Removes Arabic kasratain
    'ً': '',  # Removes Arabic fathatain
    '٬': ' ',  # Replace Arabic thousands separator with a space
    '​': '',  # Remove zero-width space
    '¬': '',  # Remove not sign
    '÷': ' ',  # Replace division sign with a space
    ']': ' ',  # Replace right square bracket with a space
    '®': '',  # Remove registered trademark symbol
    '�': '',  # Remove replacement character
    '№': ' ',  # Replace numero sign with a space
    '∆': ' ',  # Replace delta symbol with a space
    'ŭ': 'u',  # Replace u with breve to 'u'
    '[': ' ',  # Replace left square bracket with a space
    '√': ' ',  # Replace square root symbol with a space
    '﻿': '',  # Remove zero-width no-break space (BOM)
    # '/': ' ',  # Replace forward slash with a space
    'ٰ': '',  # Remove Arabic superscript alif
    '＝': ' ',  # Replace full-width equals sign with a space
    'ھ': 'ه',  # Replace Urdu/Persian 'he' with Arabic 'ه'
    '⃗': '',  # Remove combining right arrow above
    '∞': ' ',  # Replace infinity symbol with a space
    'ۍ': 'ی',  # Replace Pashto 'ye' with Persian/Arabic 'ی'
    'ە': 'ه',  # Replace Kurdish 'he' with Arabic 'ه'
    'ª': '',  # Remove feminine ordinal indicator
    'ې': 'ی',  # Replace Pashto 'ye' with Persian/Arabic 'ی'
    '‪': '',  # Remove left-to-right embedding (LRE)
    'ŧ': 't',  # Replace Latin letter 't with stroke' to 't'
    'ٱ': 'ا',  # Replace Arabic letter 'alif with wasla' to standard 'ا'
    '£': '',  # Remove pound sign
    'œ': 'oe',  # Replace Latin ligature 'oe' with 'oe',
}

sign_dict_fa_phase_two = {
    r"\u200c": " ",
    ',': '،',  # Maps comma to Persian comma
    '،': " ",  # Maps Persian comma to space
    ';': '؛',  # Maps semicolon to Persian semicolon
    '؛': ' ',  # Maps Persian semicolon to space
    '?': ' ',  # Maps question mark to Persian question mark
    '؟': ' ',  # Maps Persian question mark to space
    '!': ' ',  # Maps exclamation mark to space
    ':': ' ',  # Maps colon to space
    '...': ' ',  # Maps ellipsis to a single period surrounded by spaces
    '..': ' ',  # Maps double period to a single period surrounded by spaces
    '. . .': ' ',  # Maps spaced ellipsis to a single period surrounded by spaces
    '…': ' ',  # Maps ellipsis symbol to a single period surrounded by spaces
    '“': ' ',  # Maps left double quotation mark to space
    '”': ' ',  # Maps right double quotation mark to space
    "'": ' ',  # Maps single quote to space
    '‘': ' ',  # Maps left single quotation mark to space
    '’': ' ',  # Maps right single quotation mark to space
    '"': ' ',  # Maps double quote to space
    '(': ' ',  # Maps left parenthesis to space
    ')': ' ',  # Maps right parenthesis to space
    '-': ' ',  # Maps hyphen to space
    '—': ' ',  # Maps em dash to space
    '_': ' ',  # Maps underscore to space
    '@': '',  # Removes at symbol
    '#': '',  # Removes hashtag
    '$': '',  # Removes dollar sign
    '%': '',  # Maps percent sign to space
    '٪': '',  # Maps Persian percent sign to space
    '^': '',  # Removes caret
    '&': '',  # Removes ampersand
    '*': '',  # Removes asterisk
    '{': '',  # Removes left curly brace
    '}': '',  # Removes right curly brace
    r'\\': '',  # Removes backslash
    '`': '',  # Removes backtick
    '|': '',  # Removes pipe symbol
    '•': ' ',  # Maps bullet point to space
    '。': ' ',  # Maps Chinese period to space
    '¡': ' ',  # Maps inverted exclamation mark to space
    '¿': ' ',  # Maps inverted question mark to space
    '¨': ' ',  # Maps diaeresis to space
    '¯': ' ',  # Maps macron to space
    '°': ' ',  # Maps degree sign to space
    '±': ' ',  # Maps plus-minus sign to space
    '²': ' ',  # Maps squared sign to space
    '³': ' ',  # Maps cubed sign to space
    '´': ' ',  # Maps acute accent to space
    'µ': ' ',  # Maps micro sign to space
    '¶': ' ',  # Maps paragraph sign to space
    '·': ' ',  # Maps middle dot to space
    '¸': ' ',  # Maps cedilla to space
    '¹': ' ',  # Maps superscript one to space
    '☑': ' ',  # Maps ballot box with check to space
    '↓': ' ',  # Maps downwards arrow to space
    '➡': ' ',  # Maps rightwards arrow to space
    '⬅': ' ',  # Maps leftwards arrow to space
    '▫': ' ',  # Maps white small square to space
    '⃣': ' ',  # Maps keycap to space
    '»': ' ',  # Maps right double angle quote to space
    '«': ' ',  # Maps left double angle quote to space
    '<': ' ',  # Maps less-than sign to space
    '>': ' ',  # Maps greater-than sign to space
    '+': ' ',  # Maps plus sign to space
    '~': ' ',  # Maps tilde to space
    '=': ' ',  # Maps equals sign to space
    '×': ' ',  # Maps multiplication sign to space
    '《': ' ',  # Maps Chinese left double angle quote to space
    '》': ' ',  # Maps Chinese right double angle quote to space
    'ٔ': ' ',  # Maps Arabic mark to space
    '「': ' ',  # Maps Chinese left corner bracket to space
    '」': ' ',  # Maps Chinese right corner bracket to space
    '、': ' ',  # Maps Chinese comma to space
    '｀': ' ',  # Maps Japanese full-width grave accent to space
    '〜': ' ',  # Maps Japanese wave dash to space
    'ヽ': ' ',  # Maps Japanese iteration mark to space
    r'\n': ' ',  # Maps newline character to space
    r'\r': ' ',  # Maps carriage return character to space
    r'\t': ' ',  # Maps tab character to space
    '\\': ' ',  # Maps single backslash to space
    '‎': ' ',  # Maps left-to-right mark to space
    r'\u00A0': ' ',  # Maps non-breaking space to space
    '.': ' ',  # Maps period to space
    '–': ' ',  # Maps en dash to space
    'ّ': '',  # Removes Arabic shadda
    'َ': '',  # Removes Arabic fatha
    'ُ': '',  # Removes Arabic damma
    'ِ': '',  # Removes Arabic kasra
    'ٌ': '',  # Removes Arabic dammatain
    'ٍ': '',  # Removes Arabic kasratain
    'ً': '',  # Removes Arabic fathatain
    '٬': ' ',  # Replace Arabic thousands separator with a space
    '​': '',  # Remove zero-width space
    '¬': '',  # Remove not sign
    '÷': ' ',  # Replace division sign with a space
    ']': ' ',  # Replace right square bracket with a space
    '®': '',  # Remove registered trademark symbol
    '�': '',  # Remove replacement character
    '№': ' ',  # Replace numero sign with a space
    '∆': ' ',  # Replace delta symbol with a space
    'ŭ': 'u',  # Replace u with breve to 'u'
    '[': ' ',  # Replace left square bracket with a space
    '√': ' ',  # Replace square root symbol with a space
    '﻿': '',  # Remove zero-width no-break space (BOM)
    '/': ' ',  # Replace forward slash with a space
    'ٰ': '',  # Remove Arabic superscript alif
    '＝': ' ',  # Replace full-width equals sign with a space
    'ھ': 'ه',  # Replace Urdu/Persian 'he' with Arabic 'ه'
    '⃗': '',  # Remove combining right arrow above
    '∞': ' ',  # Replace infinity symbol with a space
    'ۍ': 'ی',  # Replace Pashto 'ye' with Persian/Arabic 'ی'
    'ە': 'ه',  # Replace Kurdish 'he' with Arabic 'ه'
    'ª': '',  # Remove feminine ordinal indicator
    'ې': 'ی',  # Replace Pashto 'ye' with Persian/Arabic 'ی'
    '‪': '',  # Remove left-to-right embedding (LRE)
    'ŧ': 't',  # Replace Latin letter 't with stroke' to 't'
    'ٱ': 'ا',  # Replace Arabic letter 'alif with wasla' to standard 'ا'
    '£': '',  # Remove pound sign
    'œ': 'oe',  # Replace Latin ligature 'oe' with 'oe',
}

# Maps a variety of special characters, symbols, accented characters, and some foreign characters to either their base form or removes them entirely.
special_char_dict = {
    '©': '',  # Removes copyright symbol
    '♫': ' ',  # Maps music note symbol to space
    '♪': ' ',  # Maps another music note symbol to space
    '‏': '',  # Removes Arabic letter mark
    'é': 'e',  # Maps accented 'e' to 'e'
    'ُ': '',  # Removes Arabic damma
    'ø': '',  # Removes Danish/Norwegian 'o' with stroke
    '—': ' ',  # Maps em dash to space
    "'": '',  # Removes apostrophe
    '&': ' ',  # Maps ampersand to space
    'σ': '',  # Removes Greek sigma
    '‘': '',  # Removes left single quotation mark
    'à': '',  # Removes accented 'a'
    '中': '',  # Removes Chinese character
    'φ': '',  # Removes Greek phi
    '’': '',  # Removes right single quotation mark
    'υ': 'u',  # Maps Greek upsilon to 'u'
    'ἐ': '',  # Removes Greek epsilon
    'ᾶ': '',  # Removes Greek alpha with macron
    'å': '',  # Removes Scandinavian 'a' with ring
    'ـ': '',  # Removes Arabic tatweel
    'ǔ': 'u',  # Maps accented 'u' to 'u'
    '所': '',  # Removes Chinese character
    '‍': '',  # Removes zero-width joiner
    'ō': 'o',  # Maps accented 'o' to 'o'
    'ó': 'o',  # Maps accented 'o' to 'o'
    'ē': 'e',  # Maps accented 'e' to 'e'
    'α': 'a',  # Maps Greek alpha to 'a'
    '−': ' ',  # Maps minus sign to space
    'ì': 'i',  # Maps accented 'i' to 'i'
    'ú': 'u',  # Maps accented 'u' to 'u'
    'á': 'a',  # Maps accented 'a' to 'a'
    'ū': 'u',  # Maps accented 'u' to 'u'
    'ǒ': 'o',  # Maps accented 'o' to 'o'
    '研': '',  # Removes Chinese character
    'μ': '',  # Removes Greek mu
    'َ': '',  # Removes Arabic fatha
    '究': '',  # Removes Chinese character
    'Å': 'a',  # Maps Scandinavian 'A' with ring to 'a'
    '毒': '',  # Removes Chinese character
    '…': '',  # Removes ellipsis
    'ł': '',  # Removes Polish 'l' with stroke
    'æ': '',  # Removes Old English letter 'ash'
    '艾': '',  # Removes Chinese character
    '芬': '',  # Removes Chinese character
    '发': '',  # Removes Chinese character
    '哨': '',  # Removes Chinese character
    '子': '',  # Removes Chinese character
    '的': '',  # Removes Chinese character
    '人': '',  # Removes Chinese character
    '!': '',  # Removes exclamation mark
    '大': '',  # Removes Chinese character
    '别': '',  # Removes Chinese character
    '山': '',  # Removes Chinese character
    '区': '',  # Removes Chinese character
    '域': '',  # Removes Chinese character
    '医': '',  # Removes Chinese character
    '疗': '',  # Removes Chinese character
    '心': '',  # Removes Chinese character
    '€': ' ',  # Maps euro sign to space
    '国': '',  # Removes Chinese character
    '科': '',  # Removes Chinese character
    '学': '',  # Removes Chinese character
    '院': '',  # Removes Chinese character
    '武': '',  # Removes Chinese character
    '汉': '',  # Removes Chinese character
    '病': '',  # Removes Chinese character
    '→': ' ',  # Maps right arrow to space
    'إ': 'ا',  # Maps Arabic 'alif with hamza below' to standard 'ا'
    'ﺎ': 'ا',  # Maps Arabic 'alif' final form to standard 'ا'
    'อ': '',  # Removes Thai character
    'ٓ': '',  # Removes Arabic superscript alif
    'ñ': 'n',  # Maps Spanish 'n with tilde' to 'n'
    'è': 'e',  # Maps accented 'e' to 'e'
    'ﻪ': 'ه',  # Maps Arabic 'he' final form to standard 'ه'
    'ร': '',  # Removes Thai character
    'ย': '',  # Removes Thai character
    r'|': r'|',  # Keeps pipe symbol
    r'`': r'`',  # Keeps backtick
    'ö': 'o',  # Maps accented 'o' to 'o'
    'ﺘ': 'ت',  # Maps Arabic 'te' to standard form 'ت'
    'ä': 'a',  # Maps accented 'a' to 'a'
    '×': 'x',  # Maps multiplication sign to 'x'
    '่': '',  # Removes Thai character
    'Á': 'A',  # Maps accented 'A' to 'A'
    '¼': '1/4',  # Maps fraction one-fourth to '1/4'
    'ˏ': '',  # Removes Greek symbol
    '¾': '3/4',  # Maps fraction three-fourths to '3/4'
    'ç': 'c',  # Maps French 'c with cedilla' to 'c'
    'ã': 'a',  # Maps Portuguese 'a with tilde' to 'a'
    '>': '>',  # Keeps greater-than sign
    '<': '<',  # Keeps less-than sign
    '?': '?',  # Keeps question mark
    'ü': 'u',  # Maps accented 'u' to 'u'
    r'^': r'^',  # Keeps caret
    'ï': 'i',  # Maps accented 'i' to 'i'
    'ô': 'o',  # Maps accented 'o' to 'o'
    '•': '',  # Removes bullet point
    'ù': 'u',  # Maps accented 'u' to 'u'
    'â': 'a',  # Maps accented 'a' to 'a'
    'ā': 'a',  # Maps accented 'a' to 'a'
    '²': '2',  # Maps superscript two to '2'
    'Ç': 'C',  # Maps French 'C with cedilla' to 'C'
    'É': 'E',  # Maps accented 'E' to 'E'
    'Ö': 'O',  # Maps accented 'O' to 'O'
    'Ō': 'O',  # Maps accented 'O' to 'O'
    'ê': 'e',  # Maps accented 'e' to 'e'
    'ë': 'e',  # Maps accented 'e' to 'e'
    'û': 'u',  # Maps accented 'u' to 'u'
    '¶': ' ',  # Maps paragraph symbol to space
    'ò': '',  # Removes accented 'o'
    'í': '',  # Removes accented 'i'
    'ν': '',  # Removes Greek nu
    'ș': '',  # Removes Romanian 's with comma'
    'β': '',  # Removes Greek beta
    'ə': '',  # Removes schwa symbol
    'ī': '',  # Removes accented 'i'
    'オ': '',  # Removes Japanese character
    'リ': '',  # Removes Japanese character
    'ン': '',  # Removes Japanese character
    'ピ': '',  # Removes Japanese character
    'ッ': '',  # Removes Japanese character
    '季': '',  # Removes Chinese character
    '封': '',  # Removes Chinese character
    '城': '',  # Removes Chinese character
    '夏': '',  # Removes Chinese character
    '年': '',  # Removes Chinese character
    'č': '',  # Removes Czech 'c with caron'
    'ク': '',  # Removes Japanese character
    '..': ' ',  # Maps double period to space
    '”': ' ',  # Maps right double quotation mark to space
    '“': ' ',  # Maps left double quotation mark to space
    "___": ' ',  # Maps triple underscore to space
    "_": ' ',  # Maps underscore to space
    '‐': ' ',  # Replace hyphen with a space
    '‫': '',  # Remove right-to-left embedding
    '‬': '',  # Remove pop directional formatting
    '­': '',  # Remove soft hyphen
    '٫': ' ',  # Replace Arabic decimal separator with a space
    '⃪': '',  # Remove combining left arrow above
    'ْ': '',  # Remove Arabic sukun
    'ّ': '',  # Remove Arabic shadda (تشديد)
    '٬': ' ',  # Replace Arabic thousands separator with a space
    '​': '',  # Remove zero-width space
    '¬': '',  # Remove not sign
    '÷': ' ',  # Replace division sign with a space
    ']': ' ',  # Replace right square bracket with a space
    '®': '',  # Remove registered trademark symbol
    '�': '',  # Remove replacement character
    '№': ' ',  # Replace numero sign with a space
    '∆': ' ',  # Replace delta symbol with a space
    'ŭ': 'u',  # Replace u with breve to 'u'
    '[': ' ',  # Replace left square bracket with a space
    '√': ' ',  # Replace square root symbol with a space
    '﻿': '',  # Remove zero-width no-break space (BOM)
    '/': ' ',  # Replace forward slash with a space
    'ٰ': '',  # Remove Arabic superscript alif
    '＝': ' ',  # Replace full-width equals sign with a space
    'ھ': 'ه',  # Replace Urdu/Persian 'he' with Arabic 'ه'
    '⃗': '',  # Remove combining right arrow above
    '∞': ' ',  # Replace infinity symbol with a space
    'ۍ': 'ی',  # Replace Pashto 'ye' with Persian/Arabic 'ی'
    'ە': 'ه',  # Replace Kurdish 'he' with Arabic 'ه'
    'ª': '',  # Remove feminine ordinal indicator
    'ې': 'ی',  # Replace Pashto 'ye' with Persian/Arabic 'ی'
    '‪': '',  # Remove left-to-right embedding (LRE)
    'ŧ': 't',  # Replace Latin letter 't with stroke' to 't'
    'ٱ': 'ا',  # Replace Arabic letter 'alif with wasla' to standard 'ا'
    '£': '',  # Remove pound sign
    'œ': 'oe',  # Replace Latin ligature 'oe' with 'oe'
}

# Maps abbreviations of month names to their full form, handling both lowercase and capitalized abbreviations.
month_dict = {
    'jan': 'january',  # Maps 'jan' to 'january'
    'feb': 'february',  # Maps 'feb' to 'february'
    'mar': 'march',  # Maps 'mar' to 'march'
    'apr': 'april',  # Maps 'apr' to 'april'
    'may': 'may',  # Maps 'may' to 'may'
    'jun': 'june',  # Maps 'jun' to 'june'
    'jul': 'july',  # Maps 'jul' to 'july'
    'aug': 'august',  # Maps 'aug' to 'august'
    'sep': 'september',  # Maps 'sep' to 'september'
    'oct': 'october',  # Maps 'oct' to 'october'
    'nov': 'november',  # Maps 'nov' to 'november'
    'dec': 'december',  # Maps 'dec' to 'december'
    'Jan': 'january',  # Maps 'Jan' to 'january'
    'Feb': 'february',  # Maps 'Feb' to 'february'
    'Mar': 'march',  # Maps 'Mar' to 'march'
    'Apr': 'april',  # Maps 'Apr' to 'april'
    'May': 'may',  # Maps 'May' to 'may'
    'Jun': 'june',  # Maps 'Jun' to 'june'
    'Jul': 'july',  # Maps 'Jul' to 'july'
    'Aug': 'august',  # Maps 'Aug' to 'august'
    'Sep': 'september',  # Maps 'Sep' to 'september'
    'Oct': 'october',  # Maps 'Oct' to 'october'
    'Nov': 'november',  # Maps 'Nov' to 'november'
    'Dec': 'december',  # Maps 'Dec' to 'december'
}
