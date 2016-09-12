#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Metadata about languages used by our model training code.  Could be used for
other things in the future.

This code is based on the language metadata from the uchardet project.
"""
from __future__ import absolute_import, print_function

from string import ascii_letters


class Language(object):
    """Metadata about a language useful for training models

    :ivar name: The human name for the language, in English.
    :type name: str
    :ivar iso_code: 2-letter ISO 639-1 if possible, 3-letter ISO code otherwise,
                    or use another catalog as a last resort.
    :type iso_code: str
    :ivar use_ascii: Whether or not ASCII letters should be included in trained
                     models.
    :type use_ascii: bool
    :ivar charsets: The charsets we want to support and create data for.
    :type charsets: list of str
    :ivar alphabet: The characters in the language's alphabet. If `use_ascii` is
                    `True`, you only need to add those not in the ASCII set.
    :type alphabet: str
    :ivar wiki_start_pages: The Wikipedia pages to start from if we're crawling
                            Wikipedia for training data.
    :type wiki_start_pages: list of str
    """
    def __init__(self, name=None, iso_code=None, use_ascii=True, charsets=None,
                 alphabet=None, wiki_start_pages=None):
        super(Language, self).__init__()
        self.name = name
        self.iso_code = iso_code
        self.use_ascii = use_ascii
        self.charsets = charsets
        if self.use_ascii:
            if alphabet:
                alphabet += ascii_letters
            else:
                alphabet = ascii_letters
        self.alphabet = alphabet
        self.wiki_start_pages = wiki_start_pages


LANGUAGES = {'Arabic': Language(name='Arabic',
                                iso_code='ar',
                                use_ascii=False,
                                charsets=['ISO-8859-6', 'WINDOWS-1256'],
                                # No alphabet. Arabic is complicated because
                                # letters have different forms (glyphs)
                                # depending on positions. Some charsets would
                                # encode glyphs while others would encode only
                                # the forms. In doubt, I will just let the
                                # defaults for now.
                                wiki_start_pages=[u'الصفحة_الرئيسية']),
             'Bulgarian': Language(name='Bulgarian',
                                   iso_code='bg',
                                   use_ascii=False,
                                   charsets=['ISO-8859-5', 'WINDOWS-1251'],
                                   alphabet=(u'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯ'
                                             u'абвгдежзийклмнопрстуфхцчшщъьюя'),
                                   wiki_start_pages=[u'Начална_страница']),
             'Czech': Language(name='Czech',
                               iso_code='cz',
                               use_ascii=True,
                               charsets=['ISO-8859-2', 'WINDOWS-1250'],
                               alphabet=u'áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ',
                               wiki_start_pages=[u'Hlavní_strana']),
             'Danish': Language(name='Danish',
                                iso_code='da',
                                use_ascii=True,
                                charsets=['ISO-8859-15', 'ISO-8859-1',
                                          'WINDOWS-1252'],
                                alphabet=u'æøåÆØÅ',
                                wiki_start_pages=[u'Forside']),
             'German': Language(name='German',
                                iso_code='de',
                                use_ascii=True,
                                charsets=['ISO-8859-1', 'WINDOWS-1252'],
                                alphabet=u'äöüßÄÖÜ',
                                wiki_start_pages=[u'Wikipedia:Hauptseite']),
             'Greek': Language(name='Greek',
                               iso_code='el',
                               use_ascii=False,
                               charsets=['ISO-8859-7', 'WINDOWS-1253'],
                               alphabet=(u'αβγδεζηθικλμνξοπρσςτυφχψωάέήίόύώ'
                                         u'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΣΤΥΦΧΨΩΆΈΉΊΌΎΏ'),
                               wiki_start_pages=[u'Πύλη:Κύρια']),
             'English': Language(name='English',
                                 iso_code='en',
                                 use_ascii=True,
                                 charsets=['ISO-8859-1', 'WINDOWS-1252'],
                                 wiki_start_pages=[u'Main_Page']),
             'Esperanto': Language(name='Esperanto',
                                   iso_code='eo',
                                   # Esperanto actually does use ASCII, but not
                                   # q, w, x, or y. So I just use the alphabet
                                   # parameter below instead.
                                   use_ascii=False,
                                   charsets=['ISO-8859-3'],
                                   alphabet=(u'abcĉdefgĝhĥijĵklmnoprsŝtuŭvz'
                                             u'ABCĈDEFGĜHĤIJĴKLMNOPRSŜTUŬVZ'),
                                   wiki_start_pages=[u'Vikipedio:Ĉefpaĝo']),
             'Spanish': Language(name='Spanish',
                                 iso_code='es',
                                 use_ascii=True,
                                 charsets=['ISO-8859-15', 'ISO-8859-1',
                                           'WINDOWS-1252'],
                                 alphabet=u'ñáéíóúüÑÁÉÍÓÚÜ',
                                 wiki_start_pages=[u'Wikipedia:Portada']),
             'French': Language(name='French',
                                iso_code='fr',
                                use_ascii=True,
                                charsets=['ISO-8859-15', 'ISO-8859-1',
                                          'WINDOWS-1252'],
                                alphabet=u'œàâçèéîïùûêŒÀÂÇÈÉÎÏÙÛÊ',
                                wiki_start_pages=[u'Wikipédia:Accueil_principal',
                                                  u'Bœuf (animal)']),
             'Hebrew': Language(name='Hebrew',
                                iso_code='he',
                                use_ascii=False,
                                charsets=['ISO-8859-8', 'WINDOWS-1255'],
                                alphabet=u'אבגדהוזחטיךכלםמןנסעףפץצקרשתװױײ',
                                wiki_start_pages=[u'עמוד_ראשי']),
             'Croatian': Language(name='Croatian',
                                  iso_code='hr',
                                  # Q, W, X, Y are only used for foreign words.
                                  use_ascii=False,
                                  charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                  alphabet=(u'abcčćdđefghijklmnoprsštuvzž'
                                            u'ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ'),
                                  wiki_start_pages=[u'Glavna_stranica']),
             'Hungarian': Language(name='Hungarian',
                                   iso_code='hu',
                                   # Q, W, X, Y are only used for foreign words.
                                   use_ascii=False,
                                   charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                   alphabet=(u'abcdefghijklmnoprstuvzáéíóöőúüű'
                                             u'ABCDEFGHIJKLMNOPRSTUVZÁÉÍÓÖŐÚÜŰ'),
                                   wiki_start_pages=[u'Kezdőlap']),
             'Polish': Language(name='Polish',
                                iso_code='pl',
                                # Q and X are only used for foreign words.
                                use_ascii=False,
                                charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                alphabet=(u'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ'
                                          u'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'),
                                wiki_start_pages=[u'Wikipedia:Strona_główna']),
             'Romanian': Language(name='Romanian',
                                  iso_code='ro',
                                  use_ascii=True,
                                  charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                  alphabet=u'ăâîșțĂÂÎȘȚ',
                                  wiki_start_pages=[u'Wikipedia:Strona_główna']),
             'Russian': Language(name='Russian',
                                 iso_code='ru',
                                 use_ascii=False,
                                 charsets=['ISO-8859-5', 'WINDOWS-1251',
                                           'KOI8-R', 'MacCyrillic', 'IBM866',
                                           'IBM855'],
                                 alphabet=(u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                           u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'),
                                 wiki_start_pages=[u'Заглавная_страница']),
             'Slovak': Language(name='Slovak',
                                iso_code='sk',
                                use_ascii=True,
                                charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                alphabet=u'áäčďéíĺľňóôŕšťúýžÁÄČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ',
                                wiki_start_pages=[u'Wikipedia:Strona_główna']),
             'Slovene': Language(name='Slovene',
                                 iso_code='sl',
                                 # Q, W, X, Y are only used for foreign words.
                                 use_ascii=False,
                                 charsets=['ISO-8859-2', 'WINDOWS-1250'],
                                 alphabet=(u'abcčdefghijklmnoprsštuvzž'
                                           u'ABCČDEFGHIJKLMNOPRSŠTUVZŽ'),
                                 wiki_start_pages=[u'Glavna_stran']),
             'Thai': Language(name='Thai',
                              iso_code='th',
                              use_ascii=False,
                              charsets=['ISO-8859-11', 'TIS-620', 'CP874'],
                              wiki_start_pages=[u'หน้าหลัก']),
             'Turkish': Language(name='Turkish',
                                 iso_code='tr',
                                 # Q, W, and X are not used by Turkish
                                 use_ascii=False,
                                 charsets=['ISO-8859-3', 'ISO-8859-9',
                                           'WINDOWS-1254'],
                                 alphabet=(u'abcçdefgğhıijklmnoöprsştuüvyzâîû'
                                           u'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZÂÎÛ'),
                                 wiki_start_pages=[u'Ana_Sayfa']),
             'Vietnamese': Language(name='Vietnamese',
                                    iso_code='vi',
                                    use_ascii=False,
                                    # From Wikipedia:
                                    # For systems that lack support for Unicode,
                                    # dozens of 8-bit Vietnamese code pages are
                                    # available.[1] The most common are VISCII
                                    # (TCVN 5712:1993), VPS, and Windows-1258.[3]
                                    # Where ASCII is required, such as when
                                    # ensuring readability in plain text e-mail,
                                    # Vietnamese letters are often encoded
                                    # according to Vietnamese Quoted-Readable
                                    # (VIQR) or VSCII Mnemonic (VSCII-MNEM),[4]
                                    # though usage of either variable-width
                                    # scheme has declined dramatically following
                                    # the adoption of Unicode on the World Wide
                                    # Web.
                                    charsets=['WINDOWS-1258', 'VISCII'],
                                    alphabet=(u'aăâbcdđeêghiklmnoôơpqrstuưvxy'
                                              u'AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY'),
                                    wiki_start_pages=[u'Chữ_Quốc_ngữ']),
            }