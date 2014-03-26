#gatestats

Uses [pelican](http://getpelican.com), [vnstat](http://humdi.net/vnstat/) and [some weird python code](https://github.com/spookey/vnstat-pelican-control) to generate a daily traffic overview.

See it in action [here](http://gatestats.freifunk-wiesbaden.de/).

See [vnstat-pelican-control](https://github.com/spookey/vnstat-pelican-control) for a list of command-line flags and how to use them.

* install and setup vnstat correctly at your gateway
* create a passwordless ssh-key for your gateway
* place it in `~/.ssh/` on your webserver
* clone this repo to your webserver
    * you do not need to run `pelican-quickstart`
    * all necessary files for pelican are in this repo (and their submodules)
* update all submodules
* symlink your webserver's document folder to pelican's output folder:

e.g.:

    ln -s /var/www/gatestats ~/software/gatestats/output

* add your gateway to the `config.py`
* setup a crontab entry

once daily, e.g.:

    23 23 * * * /usr/local/bin/python3.3 $HOME/software/gatestats/vnstat-pelican-control/main.py >> $HOME/software/gatestats/_cronjob.log 2>&1

There are no deploy-options from pelican used, the site is generated directly at the webserver.
