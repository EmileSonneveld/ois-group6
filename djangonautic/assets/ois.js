// Sync. Will throw Exceptino if something goes wrong.
function badGet(url) {
    let res = null;
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
       if (xhttp.readyState === 4)
       {
           if(xhttp.status < 200 || xhttp.status >= 300)
               throw new Error("badGet: " + xhttp.message);

           res = xhttp.responseText
           if(xhttp.getResponseHeader("Content-Type").toLowerCase().indexOf("json") !== -1)
               res = JSON.parse(res)
       }
    }
    xhttp.open("GET", url, false);
    xhttp.send();

    return res;
}