from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub():
    return TranslatorHub(
        root_locale="en",
        locales_map={
            "en": ("en",),
        },
        translators=[
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["./project/present/bot/locales/en-US/main.ftl"],
                ),
            ),
        ],
    )
