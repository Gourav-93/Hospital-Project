package com.hospital.backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hospital.backend.model.AppointmentModel;
import com.hospital.backend.repository.AppointmentRepository;

import java.util.List;

@Service
public class AppointmentService {

    @Autowired
    private AppointmentRepository appointmentRepository;

    public AppointmentModel bookAppointment(AppointmentModel appointmentmodel) {
        return appointmentRepository.save(appointmentmodel);
    }

    public List<AppointmentModel> getappointment() {
        return appointmentRepository.findAll();
    }

    public boolean existsById(Long id) {
        return appointmentRepository.existsById(id);
    }

    public void deleteAppointment(Long id) {
        appointmentRepository.deleteById(id);
    }
}
