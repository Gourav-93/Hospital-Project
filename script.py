import os

frontend_dir = r'C:\Users\Dell\OneDrive\Desktop\backend\frontend'
os.makedirs(os.path.join(frontend_dir, 'css'), exist_ok=True)
os.makedirs(os.path.join(frontend_dir, 'js'), exist_ok=True)

# 1. API.js
api_js = '''const API_BASE_URL = 'http://localhost:8080/api';

async function fetchAPI(endpoint, options = {}) {
  const url = ${API_BASE_URL};
  const defaultHeaders = { 'Content-Type': 'application/json', 'Accept': 'application/json' };
  
  try {
    const response = await fetch(url, { ...options, headers: { ...defaultHeaders, ...options.headers } });
    if (!response.ok) throw new Error(HTTP Error: );
    const text = await response.text();
    return text ? JSON.parse(text) : {};
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}

window.api = {
  getDoctors: () => fetchAPI('/doctor'),
  getDoctor: (id) => fetchAPI(/doctor/),
  createDoctor: (data) => fetchAPI('/doctor/add', { method: 'POST', body: JSON.stringify(data) }),
  deleteDoctor: (id) => fetchAPI(/doctor/delete/, { method: 'DELETE' }),

  getPatients: () => fetchAPI('/patient'),
  getPatient: (id) => fetchAPI(/patient/),
  createPatient: (data) => fetchAPI('/patient/add', { method: 'POST', body: JSON.stringify(data) }),
  deletePatient: (id) => fetchAPI(/patient/delete/, { method: 'DELETE' }),

  getAppointments: () => fetchAPI('/appointment'),
  createAppointment: (data) => fetchAPI('/appointment/add', { method: 'POST', body: JSON.stringify(data) }),
  deleteAppointment: (id) => fetchAPI(/appointment/delete/, { method: 'DELETE' })
};
'''
with open(os.path.join(frontend_dir, 'js', 'api.js'), 'w', encoding='utf-8') as f: f.write(api_js)

# 2. Main.js (Navbar and Footer injection)
main_js = '''document.addEventListener('DOMContentLoaded', () => {
  document.body.insertAdjacentHTML('afterbegin', 
    <nav class="navbar" style="padding: 1rem; background: var(--bg-card); box-shadow: 0 2px 10px rgba(0,0,0,0.1); display: flex; justify-content: space-between;">
      <a href="dashboard.html" style="font-size: 1.5rem; font-weight: bold; color: #2563EB; text-decoration: none;">MedCare</a>
      <div style="display: flex; gap: 1rem;">
        <a href="dashboard.html">Dashboard</a>
        <a href="doctors.html">Doctors</a>
        <a href="patients.html">Patients</a>
        <a href="appointments.html">Appointments</a>
      </div>
    </nav>
  );
  
  window.showToast = (msg) => alert(msg);
});
'''
with open(os.path.join(frontend_dir, 'js', 'main.js'), 'w', encoding='utf-8') as f: f.write(main_js)

# 3. CSS
style_css = '''
:root { --bg-main: #F8FAFC; --bg-card: #FFFFFF; --text-main: #1E293B; --primary: #2563EB; }
body { font-family: 'Inter', sans-serif; background: var(--bg-main); color: var(--text-main); margin: 0; display: flex; flex-direction: column; min-height: 100vh; }
.container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
.card { background: var(--bg-card); padding: 1.5rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 1rem; border-bottom: 1px solid #e2e8f0; text-align: left; }
.btn { padding: 0.5rem 1rem; background: var(--primary); color: white; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; }
.form-group { margin-bottom: 1rem; display: flex; flex-direction: column;}
input, select { padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px; }
'''
with open(os.path.join(frontend_dir, 'css', 'style.css'), 'w', encoding='utf-8') as f: f.write(style_css)

# 4. Dashboard
dashboard_html = '''<!DOCTYPE html>
<html><head><title>Dashboard</title><link rel="stylesheet" href="css/style.css"></head>
<body>
  <div class="container">
    <h1>Dashboard</h1>
    <div style="display: flex; gap: 1rem; margin-bottom: 2rem;">
      <div class="card" style="flex: 1;"><h3>Doctors</h3><p id="d-count">0</p></div>
      <div class="card" style="flex: 1;"><h3>Patients</h3><p id="p-count">0</p></div>
      <div class="card" style="flex: 1;"><h3>Appointments</h3><p id="a-count">0</p></div>
    </div>
  </div>
  <script src="js/api.js"></script><script src="js/main.js"></script>
  <script>
    async function load() {
      const docs = await window.api.getDoctors(); document.getElementById('d-count').innerText = docs.length;
      const pats = await window.api.getPatients(); document.getElementById('p-count').innerText = pats.length;
      const apts = await window.api.getAppointments(); document.getElementById('a-count').innerText = apts.length;
    }
    load();
  </script>
</body></html>'''
with open(os.path.join(frontend_dir, 'dashboard.html'), 'w', encoding='utf-8') as f: f.write(dashboard_html)

# 5. Doctors
docs_html = '''<!DOCTYPE html>
<html><head><title>Doctors</title><link rel="stylesheet" href="css/style.css"></head>
<body>
  <div class="container">
    <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
      <h1>Doctors</h1>
    </div>
    <div class="card">
      <form id="doc-form" style="display:flex; gap:1rem; margin-bottom: 1rem;">
        <input type="text" id="name" placeholder="Name" required>
        <input type="text" id="speciality" placeholder="Speciality" required>
        <input type="text" id="edu" placeholder="Education" required>
        <input type="number" id="exp" placeholder="Experience" required>
        <input type="number" id="fees" placeholder="Fees" required>
        <button type="submit" class="btn">Add Doctor</button>
      </form>
      <table>
        <thead><tr><th>Name</th><th>Speciality</th><th>Education</th><th>Exp</th><th>Fees</th><th>Action</th></tr></thead>
        <tbody id="list"></tbody>
      </table>
    </div>
  </div>
  <script src="js/api.js"></script><script src="js/main.js"></script>
  <script>
    async function load() {
      const data = await window.api.getDoctors();
      document.getElementById('list').innerHTML = data.map(d => <tr><td></td><td></td><td></td><td> Yrs</td><td>{d.fees}</td><td><button onclick="del()">Del</button></td></tr>).join('');
    }
    document.getElementById('doc-form').onsubmit = async (e) => {
      e.preventDefault();
      await window.api.createDoctor({ name: document.getElementById('name').value, speciality: document.getElementById('speciality').value, edu: document.getElementById('edu').value, exp: document.getElementById('exp').value, fees: document.getElementById('fees').value });
      load();
    };
    window.del = async (id) => { await window.api.deleteDoctor(id); load(); };
    load();
  </script>
</body></html>'''
with open(os.path.join(frontend_dir, 'doctors.html'), 'w', encoding='utf-8') as f: f.write(docs_html)

# 6. Patients
pats_html = '''<!DOCTYPE html>
<html><head><title>Patients</title><link rel="stylesheet" href="css/style.css"></head>
<body>
  <div class="container">
    <h1>Patients</h1>
    <div class="card">
      <form id="pat-form" style="display:flex; gap:1rem; margin-bottom: 1rem;">
        <input type="text" id="name" placeholder="Name" required>
        <input type="number" id="age" placeholder="Age" required>
        <input type="text" id="gender" placeholder="Gender" required>
        <input type="text" id="symptoms" placeholder="Symptoms" required>
        <button type="submit" class="btn">Add Patient</button>
      </form>
      <table>
        <thead><tr><th>Name</th><th>Age</th><th>Gender</th><th>Symptoms</th><th>Action</th></tr></thead>
        <tbody id="list"></tbody>
      </table>
    </div>
  </div>
  <script src="js/api.js"></script><script src="js/main.js"></script>
  <script>
    async function load() {
      const data = await window.api.getPatients();
      document.getElementById('list').innerHTML = data.map(d => <tr><td></td><td></td><td></td><td></td><td><button onclick="del()">Del</button></td></tr>).join('');
    }
    document.getElementById('pat-form').onsubmit = async (e) => {
      e.preventDefault();
      await window.api.createPatient({ name: document.getElementById('name').value, age: document.getElementById('age').value, gender: document.getElementById('gender').value, symptoms: document.getElementById('symptoms').value });
      load();
    };
    window.del = async (id) => { await window.api.deletePatient(id); load(); };
    load();
  </script>
</body></html>'''
with open(os.path.join(frontend_dir, 'patients.html'), 'w', encoding='utf-8') as f: f.write(pats_html)

# 7. Appointments
apts_html = '''<!DOCTYPE html>
<html><head><title>Appointments</title><link rel="stylesheet" href="css/style.css"></head>
<body>
  <div class="container">
    <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
      <h1>Appointments</h1>
      <a href="book-appointment.html" class="btn">Book New</a>
    </div>
    <div class="card">
      <table>
        <thead><tr><th>Doctor</th><th>Patient</th><th>Date</th><th>Time</th><th>Status</th><th>Action</th></tr></thead>
        <tbody id="list"></tbody>
      </table>
    </div>
  </div>
  <script src="js/api.js"></script><script src="js/main.js"></script>
  <script>
    async function load() {
      const [apts, docs, pats] = await Promise.all([window.api.getAppointments(), window.api.getDoctors(), window.api.getPatients()]);
      const docMap = {}; docs.forEach(d => docMap[d.id] = d.name);
      const patMap = {}; pats.forEach(p => patMap[p.id] = p.name);
      document.getElementById('list').innerHTML = apts.map(a => <tr><td></td><td></td><td></td><td></td><td></td><td><button onclick="del()">Del</button></td></tr>).join('');
    }
    window.del = async (id) => { await window.api.deleteAppointment(id); load(); };
    load();
  </script>
</body></html>'''
with open(os.path.join(frontend_dir, 'appointments.html'), 'w', encoding='utf-8') as f: f.write(apts_html)

# 8. Book Appointment
book_html = '''<!DOCTYPE html>
<html><head><title>Book Appointment</title><link rel="stylesheet" href="css/style.css"></head>
<body>
  <div class="container">
    <h1>Book Appointment</h1>
    <div class="card" style="max-width: 600px; margin: 0 auto;">
      <form id="book-form">
        <div class="form-group"><label>Doctor</label><select id="doctorId" required></select></div>
        <div class="form-group"><label>Patient</label><select id="patientId" required></select></div>
        <div class="form-group"><label>Date</label><input type="date" id="date" required></div>
        <div class="form-group"><label>Time</label><input type="time" id="time" required></div>
        <div class="form-group"><label>Status</label><select id="status"><option>Pending</option><option>Confirmed</option></select></div>
        <button type="submit" class="btn">Book Now</button>
      </form>
    </div>
  </div>
  <script src="js/api.js"></script><script src="js/main.js"></script>
  <script>
    async function load() {
      const [docs, pats] = await Promise.all([window.api.getDoctors(), window.api.getPatients()]);
      document.getElementById('doctorId').innerHTML = docs.map(d => <option value=""> ()</option>).join('');
      document.getElementById('patientId').innerHTML = pats.map(p => <option value=""></option>).join('');
    }
    document.getElementById('book-form').onsubmit = async (e) => {
      e.preventDefault();
      await window.api.createAppointment({ doctorId: parseInt(document.getElementById('doctorId').value), patientId: parseInt(document.getElementById('patientId').value), date: document.getElementById('date').value, time: document.getElementById('time').value, status: document.getElementById('status').value });
      window.location.href = 'appointments.html';
    };
    load();
  </script>
</body></html>'''
with open(os.path.join(frontend_dir, 'book-appointment.html'), 'w', encoding='utf-8') as f: f.write(book_html)

print("Generated frontend successfully!")
