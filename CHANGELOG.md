# Changelog

## [0.4.3](https://github.com/googleapis/python-domains/compare/v0.4.2...v0.4.3) (2022-06-07)


### Bug Fixes

* **deps:** require protobuf<4.0.0 on v0 branch ([#148](https://github.com/googleapis/python-domains/issues/148)) ([02e873c](https://github.com/googleapis/python-domains/commit/02e873cbe10c7fd76e96e7129a145e32f05457d9))

### [0.4.2](https://github.com/googleapis/python-domains/compare/v0.4.1...v0.4.2) (2022-04-01)


### Bug Fixes

* **deps:** require google-api-core >= 1.31.5, >= 2.3.2 on v0 release ([#122](https://github.com/googleapis/python-domains/issues/122)) ([8ab9667](https://github.com/googleapis/python-domains/commit/8ab966771a8b8364cdab18d953f0acb2b2319f7a))

### [0.4.1](https://www.github.com/googleapis/python-domains/compare/v0.4.0...v0.4.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([2375457](https://www.github.com/googleapis/python-domains/commit/2375457fc8772914f8689bdcfd132c15fb504d84))
* **deps:** require google-api-core >= 1.28.0 ([2375457](https://www.github.com/googleapis/python-domains/commit/2375457fc8772914f8689bdcfd132c15fb504d84))


### Documentation

* list oneofs in docstring ([2375457](https://www.github.com/googleapis/python-domains/commit/2375457fc8772914f8689bdcfd132c15fb504d84))

## [0.4.0](https://www.github.com/googleapis/python-domains/compare/v0.3.0...v0.4.0) (2021-10-21)


### Features

* add support for python 3.10 ([#74](https://www.github.com/googleapis/python-domains/issues/74)) ([320b3a0](https://www.github.com/googleapis/python-domains/commit/320b3a0ecc2ebb8ff1d1414a18d5d9f39dda1ae3))
* add v1 API, plus v1b1 methods for domain transfers ([#77](https://www.github.com/googleapis/python-domains/issues/77)) ([47434a1](https://www.github.com/googleapis/python-domains/commit/47434a15ae6205681209e668ddc358d325ac5f24))
* set v1 as the default import ([#79](https://www.github.com/googleapis/python-domains/issues/79)) ([4e2691e](https://www.github.com/googleapis/python-domains/commit/4e2691ee781d59c73fd9cb97b39dd59caac34329))


### Bug Fixes

* **deps:** require proto-plus 1.15.0 ([#81](https://www.github.com/googleapis/python-domains/issues/81)) ([1c72855](https://www.github.com/googleapis/python-domains/commit/1c72855510a51870342e2c3f039571283b7a4534))

## [0.3.0](https://www.github.com/googleapis/python-domains/compare/v0.2.3...v0.3.0) (2021-10-08)


### Features

* add context manager support in client ([#71](https://www.github.com/googleapis/python-domains/issues/71)) ([9b49d70](https://www.github.com/googleapis/python-domains/commit/9b49d7047d5a71899670d87dd522f8a83566e627))

### [0.2.3](https://www.github.com/googleapis/python-domains/compare/v0.2.2...v0.2.3) (2021-09-30)


### Bug Fixes

* improper types in pagers generation ([17d4bed](https://www.github.com/googleapis/python-domains/commit/17d4bed929328cfad16595e0c27d8cf67456f633))

### [0.2.2](https://www.github.com/googleapis/python-domains/compare/v0.2.1...v0.2.2) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([fa12c9b](https://www.github.com/googleapis/python-domains/commit/fa12c9b4f77bf43a41df5bb84e3a12c7c2b5a48f))

### [0.2.1](https://www.github.com/googleapis/python-domains/compare/v0.2.0...v0.2.1) (2021-07-28)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#42](https://www.github.com/googleapis/python-domains/issues/42)) ([8c7a8cc](https://www.github.com/googleapis/python-domains/commit/8c7a8cc2923e6bf2cec6d6447ade420632d3c95a))
* enable self signed jwt for grpc ([#47](https://www.github.com/googleapis/python-domains/issues/47)) ([d4b8730](https://www.github.com/googleapis/python-domains/commit/d4b873068ca3d0f7fadc01beee2ddfcd4f4b381a))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#43](https://www.github.com/googleapis/python-domains/issues/43)) ([2718d3b](https://www.github.com/googleapis/python-domains/commit/2718d3bbe90b019ed21437f16eafd036752beaf3))


### Miscellaneous Chores

* release as 0.2.1 ([#48](https://www.github.com/googleapis/python-domains/issues/48)) ([3567065](https://www.github.com/googleapis/python-domains/commit/35670650e12cfaa7f55156153db89bb421998688))

## [0.2.0](https://www.github.com/googleapis/python-domains/compare/v0.1.0...v0.2.0) (2021-07-01)


### Features

* add always_use_jwt_access ([#36](https://www.github.com/googleapis/python-domains/issues/36)) ([a7d1670](https://www.github.com/googleapis/python-domains/commit/a7d16704d5682c3fb17c7f0354a688871b1ba298))
* support self-signed JWT flow for service accounts ([4b24611](https://www.github.com/googleapis/python-domains/commit/4b246112d770cd4d4409b8a84a72f13713a59881))


### Bug Fixes

* add async client to %name_%version/init.py ([4b24611](https://www.github.com/googleapis/python-domains/commit/4b246112d770cd4d4409b8a84a72f13713a59881))
* **deps:** add packaging requirement ([#31](https://www.github.com/googleapis/python-domains/issues/31)) ([942b7da](https://www.github.com/googleapis/python-domains/commit/942b7dadaac43081a937eb993725d670df7519e4))
* disable always_use_jwt_access ([#39](https://www.github.com/googleapis/python-domains/issues/39)) ([7830b84](https://www.github.com/googleapis/python-domains/commit/7830b846538d3331f76cc7ca41f80b3c6f13ae45))
* exclude docs and tests from package ([#30](https://www.github.com/googleapis/python-domains/issues/30)) ([20ebc47](https://www.github.com/googleapis/python-domains/commit/20ebc4790a7ed3c0013b6ce2fa0baea760ac6b51))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-domains/issues/1127)) ([#33](https://www.github.com/googleapis/python-domains/issues/33)) ([5b9e3d5](https://www.github.com/googleapis/python-domains/commit/5b9e3d5bacf94fda61f06a35125f80683f3ac7d7)), closes [#1126](https://www.github.com/googleapis/python-domains/issues/1126)

## 0.1.0 (2021-02-01)


### Features

* generate v1beta1 ([dfa1750](https://www.github.com/googleapis/python-domains/commit/dfa1750c955be72fdae1ae209ce37929e7558626))
