import {useEffect} from "react";

export class APIClient {
    constructor(baseURL) {
        this.baseURL = "https://latikdesu.art/api/"; // с сервера
        // this.baseURL = "https://Earth_API:8000/api/"; // с docker
    }

    get(path, params) {
        try {
            const url = new URL(path, this.baseURL);
            if (params) {
                Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));
            }
            return fetch(url)
                .then(response => response.json())
                .then(data => data.scene);
        } catch (error) {
            console.error(error);
        }
    }

    async get_dialogues(path, data) {
        try {
            const url = new URL(path, this.baseURL);
            return await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(data => data.dialogues);
        } catch (error) {
            console.error(error);
        }
    }
}

// useEffect(() => {
//     fetch('http://localhost:8000/api/dialog/')
//         .then(response => response.json())
//         .then(data => setDialogues(data.dialogues));
// }, []);
//
// useEffect(() => {
//     const savedDialogues = localStorage.getItem('dialogues');
//     if (savedDialogues) {
//         setDialogues(JSON.parse(savedDialogues));
//     }
//     console.log(savedDialogues);
// }, []);
//
// useEffect(() => {
//     localStorage.setItem('dialogues', JSON.stringify(dialogues));
// }, [dialogues]);
//
//
// useEffect(() => {
//     const client = new APIClient();
//     client.get_dialogues('dialog/', {start: '0', end: '0'}).then(data => {
//         setDialogues(data);
//     })
//         .catch((error) => {
//             console.error(error);
//         });
// }, []);
//
// useEffect(() => {
//     const client = new APIClient();
//     const fetchData = () => {
//         client
//             .get_dialogues('dialog/', {start: '0', end: '0'})
//             .then((data) => {
//                 setDialogues(data);
//             })
//             .catch((error) => {
//                 console.error(error);
//             });
//     };
//     fetchData();
//     if (!dialogues || dialogues.length === 0) {
//         fetchData();
//     }
//     const intervalId = setInterval(fetchData, 5000);
//     return () => clearInterval(intervalId);
// }, []);