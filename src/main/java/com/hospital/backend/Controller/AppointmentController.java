package com.hospital.backend.Controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;

import com.hospital.backend.Model.AppointmentModel;
import com.hospital.backend.Repository.AppointmentRepository;

@RestController
@CrossOrigin("*")
public class AppointmentController {

    @Autowired
    private AppointmentRepository appointmentRepository;

    @PostMapping("/api/appointment/add")
    public AppointmentModel bookAppointment(@RequestBody AppointmentModel appointmentmodel) {
        return appointmentRepository.save(appointmentmodel);
    }

    @GetMapping("/api/appointment")
    public List<AppointmentModel> getappointment() {
        return appointmentRepository.findAll();
    }

    @DeleteMapping("/api/appointment/delete/{id}")
    public String deleteAppointment(@PathVariable Long id) {
        if (!appointmentRepository.existsById(id)) {
            return "Appointment Not Found";
        }
        appointmentRepository.deleteById(id);
        return "Appointment Deleted Successfully";
    }

}
