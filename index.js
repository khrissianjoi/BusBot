const axios = require('axios');

async function main() {
    const BusUrl = process.env.BUSURL;
    const bus_id = 4793;
    const current = {
        stopid : bus_id,
        format: 'json'
    };
    const response = await axios.get(BusUrl, {params: current});
    const busTimes = response.data['results']
    busTimes.forEach(bus => {
        console.log(bus['route'] + " " + bus['duetime'])
    });
}

main().catch(console.error);