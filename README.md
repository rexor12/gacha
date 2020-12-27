# Table of contents
- [Table of contents](#table-of-contents)
- [Overview](#overview)
- [Installation](#installation)
- [Usage example](#usage-example)
- [LogBase](#logbase)
- [EntityProviderInterface](#entityproviderinterface)
- [EntityResolverInterface](#entityresolverinterface)
- [PullProviderInterface](#pullproviderinterface)

# Overview

[gacha.py](https://github.com/rexor12/gacha.py) is a Python package that aims to provide its users a way to easily implement a [gacha](https://en.wikipedia.org/wiki/Gacha_game) system in your video game by exposing interfaces for retrieving data from persistence, transforming that data and processing it for emulating pulls/rolls.

# Installation

**Python 3.8 or higher is required**

Currently, the package isn't available in the PyPi repository, therefore you can use the following command to install it directly form the GitHub repository:

```sh
# To install the latest available version, you can specify the main branch
# Linux/macOS
python3 -m pip install -U git+https://github.com/rexor12/gacha.py.git@main

# Windows
py -3 -m pip install -U git+https://github.com/rexor12/gacha.py.git@main

# To install a stable version, you can specify the exact branch
# Linux/macOS
python3 -m pip install -U git+https://github.com/rexor12/gacha.py.git@develop/2.0

# Windows
py -3 -m pip install -U git+https://github.com/rexor12/gacha.py.git@develop/2.0

# If you're using requirements.txt, you can add the following line
git+https://github.com/rexor12/gacha.py.git@main
```

# Usage example

The below code serves as an example for setting up the gacha system and generating pulls.

Please, refer to the sample (source code) for the full implementation.

```python
# Initialize an instance of our logger implementation.
log = ConsoleLog(LogLevel.INFORMATION)

# In this case, our database comes from a JSON file, so let's instantiate the JsonEntityProvider.
entity_provider = JsonEntityProvider("./samples/res/database.json", log, [
    # It's important to pass to it the entity converters.
    # In our case, our database has items, item ranks, item types and item pools.
    ItemConverter(), ItemRankConverter(), ItemTypeConverter(), PoolConverter()
])

# The item resolver determines how to interpret item prototypes from the database.
item_resolver = SimpleItemResolver(entity_provider)

# The pull provider defines the logic of the gacha pulls. In our implementation, it takes the entity provider and the item resolver to construct its item pools.
pull_provider = SimplePullProvider(entity_provider, item_resolver, log)
# If you don't like the default pull count limitation, you can set it after initialization.
pull_provider.pull_count_min = 2
pull_provider.pull_count_max = 5

# Now that everything has been set up, we can pull some items. :)
for pull in pull_provider.pull("common", 10):
    log.info("{} x{}{}".format(pull.name, pull.count, " (Rare)" if pull.is_rare else ""))
```

# LogBase

An abstract base class for a log message writer. In case you already have a logging system, you can create a simple implementation for this class that routes the requests from the package to your logger implementation.

Currently, the following implementations are available:
- **EmptyLog**: It drops every request, thus no log messages are written anywhere. It can be useful for both unit testing purposes or in case you wouldn't like to have any logs written.
- **ConsoleLog**: It simply prints every log message (according to the log level) to the console via Python's [print()](https://docs.python.org/3/library/functions.html#print) method.

# EntityProviderInterface

This interface defines methods for retrieving entities (items, ranks, types, pools, etc.) from a database.

Currently, the following implementations are available:
- **JsonEntityProvider**: Provides methods for retrieving entities from a JSON file.

# EntityResolverInterface

This interface define methods for resolving item prototypes defined in the database to virtual items in the memory.

In the case of certain games, the item prototypes defined in the database may spawn multiple virtual items (such as top, middle and bottom slots for a tattoo), therefore an item resolver can be used to transform the prototypes to the actual virtual items.

Currently, the following implementations are available:
- **SimpleItemResolver**: Resolves each item prototype to an equal virtual item without spawning additional variations.

# PullProviderInterface

This interface defines methods for generating pulls from the gacha loot tables. Unless you have some special logic for this purpose, you can use the default implementation that uses rectangular distribution among the items of a single loot table.

Currently, the following implementations are available:
- **SimplePullProvider**: Uses rectangular distribution among the items of a single loot table.