const jimp = require('jimp');
const argv = require('yargs').argv;

if (argv.path && argv.icons) {
    console.log("Resizing image @", argv.path);
    const imagePath = argv.path;
    console.log("Resizing to chrome extension icons");
    jimp.read(imagePath, (err, image) => {
        if (err) throw err;
        const imageName = imagePath.split('/')[0].split('.')[0];
        image.resize(128, 128)
            .write(`${imageName}128.png`);
        image.resize(48, 48)
            .write(`${imageName}48.png`);
        image.resize(19, 19)
            .write(`${imageName}19.png`);
        image.resize(16, 16)
            .write(`${imageName}16.png`);
    });
}
