const mainForm = document.getElementById('main-form');
const sortingForm = document.getElementById('sorting-form');
const sortAlgorithm = document.getElementById('sort-algorithm');
const sortBy = document.getElementById('sort-by');
const sortOrder = document.getElementById('sort-order');
const search = document.getElementById('search-val');
const searchAlgorithm = document.getElementById('search-algorithm');

// showcase transitions
const left = document.querySelector('.left');
const right = document.querySelector('.right');
const container = document.querySelector('.container');

left.addEventListener('mouseenter',() => {
  container.classList.add('hover-left');
})

left.addEventListener('mouseleave',() => {
    container.classList.remove('hover-left');
})

right.addEventListener('mouseenter',() => {
    container.classList.add('hover-right');
})

right.addEventListener('mouseleave',() => {
    container.classList.remove('hover-right');
})


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
    <button class="del-btn" onclick={deleteStudent("${student._id}")}>X</button>
    `;
    tableBody.appendChild(row);
  })}else{
    const row = document.createElement('tr');
    row.innerHTML = `<td colspan="13">Nothing was found</td>`;
    tableBody.appendChild(row);
  }
}

function updateLocal(){
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
}

var storedSortOrder = localStorage.getItem('sortOrder');
var storedSortAlgorithm = localStorage.getItem('sortAlgorithm');
var storedSortBy = localStorage.getItem('sortBy');
var storedsearchAlgorithm = localStorage.getItem('searchAlgorithm');
updateLocal()

if (storedSortOrder) {
  const requestData = {
    sortAlgorithm: sortAlgorithm.value || storedSortAlgorithm,
    sortBy: sortBy.value || storedSortBy,
    sortOrder: sortOrder.value || storedSortOrder,
    searchAlgorithm: searchAlgorithm.value || storedsearchAlgorithm
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
    });
}


search.addEventListener('keydown', e=>{
  if(e.key === 'Enter'){
    e.preventDefault();
  }
})


function searchStudent(e) {
  e.preventDefault();
  const requestData = {
    searchTerm: e.target.value == '' ? 'student' : e.target.value,
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
    });
}

function deleteStudent(studentid) {
  confirm('Are you sure you want to delete this student????')

  const requestData = {
    sortAlgorithm: sortAlgorithm.value || storedSortAlgorithm,
    sortBy: sortBy.value || storedSortBy,
    sortOrder: sortOrder.value || storedSortOrder,
    studentId: studentid
  };
  fetch('/delete', {
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
    });
}


function sortByCol(col){
  localStorage.setItem('sortBy', col);
  updateLocal()
  
  const requestData = {
    sortAlgorithm:   storedSortAlgorithm,
    sortBy: col,
    sortOrder:  storedSortOrder,
    searchAlgorithm:  storedsearchAlgorithm
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

var backArrow = document.getElementById('back-arrow');
var section1 = document.getElementById('showcase');
var section2 = document.getElementById('query-implementation');
var section3 = document.getElementById('registration-form');
var lastScrollPosition = document.documentElement.scrollTop;

function toggleBackArrowVisibility() {
  var currentScrollPosition = document.documentElement.scrollTop;

  if (currentScrollPosition <= section1.offsetTop) {
    backArrow.classList.remove('show');
  } else {
    backArrow.classList.add('show');
  }

  lastScrollPosition = currentScrollPosition;
}

section1.addEventListener('click', function() {
  backArrow.classList.add('show');
});

section2.addEventListener('click', function() {
  backArrow.classList.remove('show');
});

section3.addEventListener('click', function() {
  backArrow.classList.remove('show');
});

window.addEventListener('scroll', toggleBackArrowVisibility);