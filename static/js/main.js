document.addEventListener('DOMContentLoaded', () => {
  // Get the sorting form
  const sortingForm = document.getElementById('sorting-form');
  const sortAlgorithm = document.getElementById('sort-algorithm');
  const sortBy = document.getElementById('sort-by');
  const sortOrder = document.getElementById('sort-order');
  const search = document.getElementById('search-val');

  // Add change event listener for form submission
  sortingForm.addEventListener('submit', submitForm);
  sortAlgorithm.addEventListener('change', submitForm);
  sortBy.addEventListener('change', submitForm);
  sortOrder.addEventListener('change', submitForm);
  search.addEventListener('keyup', searchStudent);
  search.addEventListener('event.key === "Enter"', searchStudent);

  function submitForm(e) {
    e.preventDefault();
    const requestData = {
      sortAlgorithm: sortAlgorithm.value,
      sortBy: sortBy.value,
      sortOrder: sortOrder.value
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




function searchStudent(e) {
  const requestData = {
    searchTerm: e.target.value
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


