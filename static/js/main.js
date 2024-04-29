document.addEventListener('DOMContentLoaded', () => {
  // Get the sorting form
  const sortingForm = document.getElementById('sorting-form');
  const sortAlgorithm = document.getElementById('sort-algorithm');
  const sortBy = document.getElementById('sort-by');
  const sortOrder = document.getElementById('sort-order');
  const search = document.getElementById('search-val');
  const searchAlgorithm = document.getElementById('search-algorithm');

  // Add change event listener for form submission
  sortingForm.addEventListener('submit', submitForm);
  sortAlgorithm.addEventListener('change', submitForm);
  sortBy.addEventListener('change', submitForm);
  sortOrder.addEventListener('change', submitForm);
  search.addEventListener('keyup', searchStudent);
  search.addEventListener('event.key === "Enter"', searchStudent);
  searchAlgorithm.addEventListener('change', searchStudent);

  function submitForm(e) {
    e.preventDefault();
    const requestData = {
      sortAlgorithm: sortAlgorithm.value,
      sortBy: sortBy.value,
      sortOrder: sortOrder.value
    };
    
    localStorage.setItem('sortAlgorithm', sortAlgorithm.value);
    localStorage.setItem('sortBy', sortBy.value);
    localStorage.setItem('sortOrder', sortOrder.value);
    localStorage.setItem('searchAlgorithm', searchAlgorithm.value)


    fetch('/sort', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestData)
    })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Request failed');
        }
      })
      .then(data => {
        updateTable(data);
      })
      .catch(error => {
        console.error('Request error:', error);
        // Handle the error here, e.g., display an error message to the user
      });
  }

function updateTable(data) {
  const tableBody = document.querySelector("#student-table tbody");

  // Clear existing rows from the table
  tableBody.innerHTML = '';
  
  if (data.length > 0) {
  num = 1
  data.forEach(student => {
    const row = document.createElement('tr');
    
    row.innerHTML = `
    <td>${ num ++ }</td>
    <td>${student.firstname}</td>
    <td>${student.lastname}</td>
    <td>${student.date_of_birth}</td>
    <td>${student.gender}</td>
    <td>${student.contact_number}</td>
    <td>${student.email}</td>
    <td>${student.address}</td>
    <td>${student.program}</td>
    <td>${student.gpa}</td>
    <td>${student.accommodation}</td>
  
    `;
    tableBody.appendChild(row);
  })}else{
    const row = document.createElement('tr');
    row.innerHTML = `<td colspan="13">Nothing was found</td>`;
    tableBody.appendChild(row);
  }
}


 // Retrieve stored values from local storage
if (localStorage.getItem('sortAlgorithm')) {
  sortAlgorithm.value = localStorage.getItem('sortAlgorithm');
}

if (localStorage.getItem('sortBy')) {
  sortBy.value = localStorage.getItem('sortBy');
}

if (localStorage.getItem('sortOrder')) {
  sortOrder.value = localStorage.getItem('sortOrder');
}
if (localStorage.getItem('searchAlgorithm')) {
  searchAlgorithm.value = localStorage.getItem('searchAlgorithm');
}


const storedSortOrder = localStorage.getItem('sortOrder');
const storedSortAlgorithm = localStorage.getItem('sortAlgorithm');
const storedSortBy = localStorage.getItem('sortBy');
const storedsearchAlgorithm = localStorage.getItem('searchAlgorithm');

if (storedSortOrder) {
  const requestData = {
    sortAlgorithm: sortAlgorithm.value | storedSortAlgorithm,
    sortBy: sortBy.value | storedSortBy,
    sortOrder: sortOrder.value | storedSortOrder,
    searchAlgorithm: searchAlgorithm.value | storedsearchAlgorithm
  };

  fetch('/sort', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
  })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Request failed');
      }
    })
    .then(data => {
      updateTable(data);
    })
    .catch(error => {
      console.error('Request error:', error);
      // Handle the error here, e.g., display an error message to the user
    });
}








function searchStudent(e) {
  const requestData = {
    searchTerm: e.target.value,
    sortOrder: localStorage.getItem('sortOrder'),
    sortAlgorithm: localStorage.getItem('sortAlgorithm'),
    sortBy: localStorage.getItem('sortBy'),
    searchAlgorithm: searchAlgorithm.value
  };

  fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
  })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Request failed');
      }
    })
    .then(data => {
      updateTable(data);
    })
    .catch(error => {
      console.error('Request error:', error);
      // Handle the error here, e.g., display an error message to the user
    });
}


});


