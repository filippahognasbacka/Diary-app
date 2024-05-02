function deleteEntry(entryId) {
    fetch("/delete-entry", {
        method: 'POST',
        body: JSON.stringify({ entryId: entryId }),
    })
    .then(function(_res) {
        window.location.href = "/";
    });
}