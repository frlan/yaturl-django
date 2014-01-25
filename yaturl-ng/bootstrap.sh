#!/bin/bash -e

VIRTUALENV_OPTS=""
while [ -n "$*" ]
do
	case $1 in
		-p|--pypy)
		VIRTUALENV_OPTS="${VIRTUALENV_OPTS} --python=$(which pypy)"
		;;
	esac
	shift
done

# use virtualenv2 on ArchLinux to enforce Python 2.x
VIRTUALENV=$(which virtualenv2 2>/dev/null)
if [ ! "${VIRTUALENV}" ]; then
	VIRTUALENV=$(which virtualenv)
fi


function log
{
	GREEN="\E[32m"
	RESET="\033[00;00m"
	echo -e "${GREEN}$1${RESET}"
}


log "Create virtualenv"
${VIRTUALENV} ${VIRTUALENV_OPTS} --distribute --no-site-packages venv

log "Activate virtualenv"
source venv/bin/activate

# update base packages
log "Update virtualenv"
pip install --upgrade pip
pip install --upgrade flup wsgiref distribute


log "Install required packages"
pip install -r requirements.txt

echo
echo "Activate: source venv/bin/activate"

log "Done."
