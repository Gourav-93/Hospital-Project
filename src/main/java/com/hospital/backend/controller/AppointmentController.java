package com.hospital.backend.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;

import com.hospital.backend.model.AppointmentModel;
import com.hospital.backend.service.AppointmentService;

@RestController
@CrossOrigin("*")
public class AppointmentController {

    @Autowired
    private AppointmentService appointmentService;

    @PostMapping("/api/appointment/add")
    public AppointmentModel bookAppointment(@RequestBody AppointmentModel appointmentmodel) {
        return appointmentService.bookAppointment(appointmentmodel);
    }

    @GetMapping("/api/appointment")
    public List<AppointmentModel> getappointment() {
        return appointmentService.getappointment();
    }

    @DeleteMapping("/api/appointment/delete/{id}")
    public String deleteAppointment(@PathVariable Long id) {
        if (!appointmentService.existsById(id)) {
            return "Appointment Not Found";
        }
        appointmentService.deleteAppointment(id);
        return "Appointment Deleted Successfully";
    }

}
