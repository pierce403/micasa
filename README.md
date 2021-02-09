# micasa
Simple python script for importing keys from the back of casascius coins.

https://en.bitcoin.it/wiki/Casascius_physical_bitcoins
https://en.bitcoin.it/wiki/Mini_private_key_format

Edit the script to put in your shortkey (line 12), then run with python2.

```
$ python micasa.py 
raw key:   4c7a9640c72dc2099f23715d0c8a0d8a35f8906e3cab61dd3f78b67bf887c9ab
check key: 000f2453798ad4f951eecced2242eaef3e1cbc8a7c813c203ac7ffe57060355d
CONGRATS!  Checksum looks good!

btc key:   5JPy8Zg7z4P7RSLsiqcqyeAF1935zjNUdMxcDeVrtU1oarrgnB7
```

This key will import to almost any wallet, including BCH and BSV wallets.

It's annoying that I even had to write this, but sometimes Electrum just isn't the right option.
If using the Electrum wallet works for you, that is likely a more convenient way to import.
