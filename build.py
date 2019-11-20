#!/usr/bin/env python3
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(\
        username="dssl",
        channel='ci',
        build_policy='missing',
    )

    builder.add_common_builds()
    builder.run()
