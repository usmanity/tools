var file = require('../sources/failed_banks.json');

var parsedData = [];

for (var i in file) {
    var year = file[i]['Closing Date'].split('-')[2];
    var strYear = year.toString();
    strYear = ` 20${strYear}`;
    if (!parsedData[strYear]) {
        parsedData[strYear] = 1;
    } else {
        parsedData[strYear]++;
    }
}

console.log(parsedData);
