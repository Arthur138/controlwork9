    async function makeRequest(url, method='GET') {
        let response = await fetch(url, {method});

        if (response.ok) {
            return await response.json();
        } else {
            let error = new Error(response.statusText);
            error.response = response;
            throw error;
        }
    }

    async function buttonClick(event) {
        let target = event.target;
        let url =target.dataset.link;
        let id = target.dataset.pk;
        let response = await makeRequest(url);
        // let div = document.getElementsByClassName('card');
        let ads = document.getElementById(`div_${id}`)
        ads.removeChild(ads.firstElementChild)

    }




