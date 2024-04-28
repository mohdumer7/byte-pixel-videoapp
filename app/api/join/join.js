'use strict';

async function getJoin() {
    try {
        // Use dynamic import with await
        const { default: fetch } = await import('node-fetch');

        const API_KEY_SECRET = 'bytepixelsfu_default_secret';
        const bytepixel_URL = 'https://sfu.bytepixel.com/api/v1/join';
        //const bytepixel_URL = 'http://localhost:3010/api/v1/join';

        const response = await fetch(bytepixel_URL, {
            method: 'POST',
            headers: {
                authorization: API_KEY_SECRET,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                room: 'test',
                roomPassword: false,
                name: 'bytepixelsfu',
                audio: true,
                video: true,
                screen: true,
                hide: false,
                notify: true,
                token: {
                    username: 'username',
                    password: 'password',
                    presenter: true,
                    expire: '1h',
                },
            }),
        });
        const data = await response.json();
        if (data.error) {
            console.log('Error:', data.error);
        } else {
            console.log('join:', data.join);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

getJoin();
