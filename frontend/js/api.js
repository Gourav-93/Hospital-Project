const API_BASE_URL = 'http://localhost:8080/api';

async function fetchAPI(endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;
  const defaultHeaders = { 'Content-Type': 'application/json', 'Accept': 'application/json' };
  try {
    const response = await fetch(url, { ...options, headers: { ...defaultHeaders, ...options.headers } });
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    const text = await response.text();
    return text ? JSON.parse(text) : {};
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}

window.api = {
  getDoctors: () => fetchAPI('/doctor'),
  getDoctor: (id) => fetchAPI(`/doctor/${id}`),
  createDoctor: (data) => fetchAPI('/doctor/add', { method: 'POST', body: JSON.stringify(data) }),
  deleteDoctor: (id) => fetchAPI(`/doctor/delete/${id}`, { method: 'DELETE' }),

  getPatients: () => fetchAPI('/patient'),
  getPatient: (id) => fetchAPI(`/patient/${id}`),
  createPatient: (data) => fetchAPI('/patient/add', { method: 'POST', body: JSON.stringify(data) }),
  deletePatient: (id) => fetchAPI(`/patient/delete/${id}`, { method: 'DELETE' }),

  getAppointments: () => fetchAPI('/appointment'),
  createAppointment: (data) => fetchAPI('/appointment/add', { method: 'POST', body: JSON.stringify(data) }),
  deleteAppointment: (id) => fetchAPI(`/appointment/delete/${id}`, { method: 'DELETE' })
};
