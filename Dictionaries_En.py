# Maps different forms of Latin letters (including small caps and other variants) to their standard lowercase English equivalent.
english_dict = {
    'ᴀ': 'a',  # Maps small capital A to lowercase 'a'
    'b': 'b',  # Maps lowercase 'b' to itself
    'ʙ': 'b',  # Maps small capital B to lowercase 'b'
    'c': 'c',  # Maps lowercase 'c' to itself
    'ᴄ': 'c',  # Maps small capital C to lowercase 'c'
    'd': 'd',  # Maps lowercase 'd' to itself
    'ᴅ': 'd',  # Maps small capital D to lowercase 'd'
    'e': 'e',  # Maps lowercase 'e' to itself
    'ᴇ': 'e',  # Maps small capital E to lowercase 'e'
    'f': 'f',  # Maps lowercase 'f' to itself
    'ꜰ': 'f',  # Maps small capital F to lowercase 'f'
    'g': 'g',  # Maps lowercase 'g' to itself
    'ɢ': 'g',  # Maps small capital G to lowercase 'g'
    'ʜ': 'h',  # Maps small capital H to lowercase 'h'
    'i': 'i',  # Maps lowercase 'i' to itself
    'ɪ': 'i',  # Maps small capital I to lowercase 'i'
    'ᴊ': 'j',  # Maps small capital J to lowercase 'j'
    'j': 'j',  # Maps lowercase 'j' to itself
    'k': 'k',  # Maps lowercase 'k' to itself
    'ᴋ': 'k',  # Maps small capital K to lowercase 'k'
    'l': 'l',  # Maps lowercase 'l' to itself
    'ʟ': 'l',  # Maps small capital L to lowercase 'l'
    'm': 'm',  # Maps lowercase 'm' to itself
    'ᴍ': 'm',  # Maps small capital M to lowercase 'm'
    'n': 'n',  # Maps lowercase 'n' to itself
    'ɴ': 'n',  # Maps small capital N to lowercase 'n'
    'o': 'o',  # Maps lowercase 'o' to itself
    'ᴏ': 'o',  # Maps small capital O to lowercase 'o'
    'ᴘ': 'p',  # Maps small capital P to lowercase 'p'
    'p': 'p',  # Maps lowercase 'p' to itself
    'q': 'q',  # Maps lowercase 'q' to itself
    'r': 'r',  # Maps lowercase 'r' to itself
    'ʀ': 'r',  # Maps small capital R to lowercase 'r'
    's': 's',  # Maps lowercase 's' to itself
    'ꜱ': 's',  # Maps small capital S to lowercase 's'
    't': 't',  # Maps lowercase 't' to itself
    'ᴛ': 't',  # Maps small capital T to lowercase 't'
    'u': 'u',  # Maps lowercase 'u' to itself
    'ᴜ': 'u',  # Maps small capital U to lowercase 'u'
    'v': 'v',  # Maps lowercase 'v' to itself
    'ᴠ': 'v',  # Maps small capital V to lowercase 'v'
    'w': 'w',  # Maps lowercase 'w' to itself
    'ᴡ': 'w',  # Maps small capital W to lowercase 'w'
    'x': 'x',  # Maps lowercase 'x' to itself
    'y': 'y',  # Maps lowercase 'y' to itself
    'ʏ': 'y',  # Maps small capital Y to lowercase 'y'
    'z': 'z'   # Maps lowercase 'z' to itself
}

# Expands English contractions into their full form.
contractions_dict = {
    "ain't": "are not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I had",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it had",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that had",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there had",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they had",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
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
    '-': ' ',  # Maps hyphen to hyphen surrounded by spaces
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
    '/': '',  # Removes forward slash
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
sign_dict_fa = {
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
    'َ': '',  # Removes Arabic fatha
    'ُ': '',  # Removes Arabic damma
    'ِ': '',  # Removes Arabic kasra
    'ٌ': '',  # Removes Arabic dammatain
    'ٍ': '',  # Removes Arabic kasratain
    'ً': '',  # Removes Arabic fathatain
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
    'jan ': 'january',
    'Jan ': 'january',
    'feb ': 'february',
    'Feb ': 'february',
    'mar ': 'march',
    'Mar ': 'march',
    'apr ': 'april',
    'Apr ': 'april',
    'may ': 'may',
    'May ': 'may',
    'jun ': 'june',
    'Jun ': 'june',
    'jul ': 'july',
    'Jul ': 'july',
    'aug ': 'august',
    'Aug ': 'august',
    'sep ': 'september',
    'Sep ': 'september',
    'oct ': 'october',
    'Oct ': 'october',
    'nov ': 'november',
    'Nov ': 'november',
    'dec ': 'december',
    'Dec ': 'december',
}
