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

import com.hospital.backend.model.PatientModel;
import com.hospital.backend.service.PatientService;

@RestController
@CrossOrigin("*")
public class PatientController {

    @Autowired
    private PatientService patientService;

    @PostMapping("/api/patient/add")
    public PatientModel addPatient(@RequestBody PatientModel pateintModel) {
        return patientService.addPatient(pateintModel);
    }

    @GetMapping("/api/patient")
    public List<PatientModel> getPatient() {
        return patientService.getPatient();
    }

    @DeleteMapping("/api/patient/delete/{id}")
    public String deletePatient(@PathVariable Long id) {

        if (!patientService.existsById(id)) {
            return "Patient Not Found";
        }

        patientService.deletePatient(id);
        return "Patient Deleted Successfully";
    }

}
