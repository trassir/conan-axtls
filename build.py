#!/usr/bin/env python3
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(
        username="trassir",
        channel='ci',
        build_policy='missing',
        login_username='trassir-ci-bot',
        upload='https://api.bintray.com/conan/trassir/conan-public'
    )

    builder.add_common_builds()
    builder.run()
