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
            return  await fetch(url, {
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