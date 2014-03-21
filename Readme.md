#gatestats

Uses [pelican](http://getpelican.com), [vnstat](http://humdi.net/vnstat/) and [some weird python code](https://github.com/spookey/vnstat-pelican-control) to generate a daily traffic overview.

See it in [action](http://gatestats.freifunk-wiesbaden.de/).

##setup

* install and setup vnstat correctly at your gateway
* create a passwordless ssh-key for your gateway
* place it in `~/.ssh/` on your webserver
* clone this repo to your webserver
* update all submodules
* symlink your webserver's output folder to pelican's:

e.g.: 

    ln -s /var/www/gatestats ~/software/gatestat/output

* add your gateway to the `config.py`

There are no deploy-options from pelican used, the site is generated directly at the webserver.

