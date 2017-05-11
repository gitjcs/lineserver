
BASEDIR="$( cd "$( dirname "$0" )" && pwd )"

# Process the file
python $BASEDIR/process_file.py $1

if [ $? -ne 0 ] ; then
    echo 'Errors processing file.'
    exit 1
fi

# Launch the service
python $BASEDIR/app/lineserver_app.py
