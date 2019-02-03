#!/usr/bin/env node
// this file is very specific on purpose
// it's used as a quick fave changer

const fs = require('fs');
const argv = require('yargs').argv;
const spawn = require('child_process').spawn;

// constants
const FAVE_FILEPATH = '/Users/muhammad/github/usmanity.github.com/fave.html';

const addFavorite = (fave) => {
    fs.exists(FAVE_FILEPATH, (exists) => {
        if (!exists) {
            console.error('fave.html file does not exist');
            return;
        }
        fs.readFile(FAVE_FILEPATH, 'utf8', (err, data) => {
            if (err) throw err;
            var lines = data.split('\n');
            lines.forEach((line, index, lines) => {
                lines[index] = checkAndUpdateLine(line, fave);
            });
            modifiedData = lines.join('\n');
            fs.writeFile(FAVE_FILEPATH, modifiedData, (err) => {
                if (err) throw err;
                console.log(`Updated fave to ${fave}`);
            });
        });

    });
}

const checkAndUpdateLine = (line, fave) => {
    let tempLine = line;
    if (tempLine.includes('window.location')) {
        tempLine = `window.location = "${fave}"`;
    }
    return tempLine;
}

if (argv.f) {
    console.log(`Adding ${argv.f} as new favorite`);
    addFavorite(argv.f);
} else if (argv._[0]) {
    console.log(`Adding ${argv._[0]} as new favorite`);
    addFavorite(argv._[0]);
} else {
    console.error('Please pass a favorite by using the -f flag');
}


