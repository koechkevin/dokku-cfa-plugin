# cfa-plugin Dokku Plugin

The `cfa-plugin` is a Dokku plugin that provides additional functionality for your Dokku apps. It requires Python to be installed and the scripts provided by the plugin are written in Python.

## Prerequisites

- [Dokku](https://dokku.com/docs/development/plugin-triggers)
- [Python](https://www.python.org/downloads/)

## Installation

```bash
dokku plugin:install https://github.com/CodeForAfrica/dokku-cfa-plugin.git
```

## Usage

### Environment Variables

Environment variables that are specific to the plugin should start with the prefix `HOOK_`.
For example, you might use environment variables like:

```
HOOK_MONGODB_URL=mongodb://root:rootpassword@localhost:27017/codeforafrica?authSource=admin
HOOK_DESTROY_DB=1
```

Setting this on any app config will destroy a mongodb url of the specified `HOOK_MONGODB_URL` on delete

## Contributing

To contribute, clone the repository and add your scripts
