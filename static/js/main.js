document.addEventListener('DOMContentLoaded', () => {
  // Get the sorting form
  const sortingForm = document.getElementById('sorting-form');
  const sortAlgorithm = document.getElementById('sort-algorithm');
  const sortBy = document.getElementById('sort-by');
  const sortOrder = document.getElementById('sort-order');

  // Add event listener for form submission
  sortAlgorithm.addEventListener('change', submitForm);
  sortBy.addEventListener('change', submitForm);
  sortOrder.addEventListener('change', submitForm);

  function submitForm(e) {
    e.preventDefault();
    const requestData = {
      algorithm: sortAlgorithm.value,
      sortBy: sortBy.value,
      sortOrder: sortOrder.value
    };
    console.log(JSON.stringify(requestData));
    fetch('/portal', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestData)
    })
    .then(response => {
      if (response.ok) {
        console.log('Request successful');
      } else {
        throw new Error('Request failed');
      }
    })
    .catch(error => {
      console.error('Request error:', error);
    });
  }
});