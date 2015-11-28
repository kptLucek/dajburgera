#!/bin/sh

usage()
{
    echo "Type: [dep.sh -i] to clear cache, run assetic and copy needed files - windows"
    echo "Type: [dep.sh -c] to clear cache, run assetic and copy needed files"
    echo "Type: [dep.sh -h] to display this help"
}

if [ "$#" = "0" ]
then
    echo "BRAK"
    # usage
    exit
fi

while getopts ich option
do
    case "${option}"
    in
        i)
            echo "Done"
            ;;
        c)
            rm -rf web/js/*
            rm -rf web/css/*
            echo "--------------------------------------------------------------------------------------------------------"
            echo "Clearing cache"
            echo "--------------------------------------------------------------------------------------------------------"
            php app/console cache:clear --env=prod
            php app/console cache:clear --env=dev
            echo "--------------------------------------------------------------------------------------------------------"
            echo "Installing assets"
            echo "--------------------------------------------------------------------------------------------------------"
            php app/console assets:install
            echo "--------------------------------------------------------------------------------------------------------"
            echo "Dumping Routes"
            echo "--------------------------------------------------------------------------------------------------------"
            php app/console fos:js-routing:dump

            echo "--------------------------------------------------------------------------------------------------------"
            echo "Warming up cache"
            echo "--------------------------------------------------------------------------------------------------------"
            php app/console cache:warmup --env=dev
            php app/console cache:warmup --env=prod
            echo "--------------------------------------------------------------------------------------------------------"
            echo "CHMOD cache dirs"
            echo "--------------------------------------------------------------------------------------------------------"
            chmod -R 777 app/cache/
            chmod -R 777 app/logs/
            echo "Done"
            ;;
        h)
            usage
            ;;
        ?)
            usage
            ;;
    esac
done
