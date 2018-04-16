# Commit Label

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

## :page_facing_up: Overview

The **commit-label** install the git **prepare-commit-msg** hook to put a label beginning of the commit message.

## :scroll: List of the Labels


* **WROTE** - Use when wrote the document such as `README`.
* **FIXED** - Use when fixed the bugs or issues.
* **IMPLEMENTED** - Use when added the new feature.
* **ENHANCED** - Use when implemented feature enhanced.
* **TESTED** - Use when wrote the unit test.
* **RELEASED** - Use when released to the product.

## :wrench: Usage

### 1. Install hook

```
$ commit-label init
done.
```

### 2. Commit

```
$ git commit -m "README.md"
Select Commit Label
1) WROTE - Use when wrote the document such as `README`.
2) FIXED - Use when fixed the bugs or issues.
3) IMPLEMENTED - Use when added the new feature.
4) ENHANCED - Use when implemented feature enhanced.
5) TESTED - Use when wrote the unit test.
6) ELEASED - Use when released to the product.
7) DO NOT PUT A LABEL
> 1
[master (root-commit) 311f3b4] WROTE: README.md
 1 file changed, 1 insertion(+)
  create mode 100644 README.md
```


## :inbox_tray: Installation

```
$ git clone git@github.com:alice1017/commit-label.git
$ cd commit-label
$ python setup.py build install
```
