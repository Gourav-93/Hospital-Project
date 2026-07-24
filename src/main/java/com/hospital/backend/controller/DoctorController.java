package com.hospital.backend.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.hospital.backend.model.DoctorModel;
import com.hospital.backend.service.DoctorService;

@RestController
@CrossOrigin(origins = "*")
public class DoctorController {

    @Autowired
    private DoctorService doctorService;

    @PostMapping("/api/doctor/add")
    public DoctorModel addDoctor(@RequestBody DoctorModel doctorModel) {
        return doctorService.addDoctor(doctorModel);
    }

    @GetMapping("/api/doctor")
    public List<DoctorModel> getDoctors() {
        return doctorService.getDoctors();
    }

    @DeleteMapping("/api/doctor/delete/{id}")
    public String deleteDoctor(@PathVariable Long id) {

        if (!doctorService.existsById(id)) {
            return "Doctor Not Found";
        }

        doctorService.deleteDoctor(id);
        return "Doctor Deleted Successfully";
    }

}
