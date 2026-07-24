package com.hospital.backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.hospital.backend.model.PatientModel;
import com.hospital.backend.repository.PatientRepository;

import java.util.List;

@Service
public class PatientService {

    @Autowired
    private PatientRepository patientRepository;

    public PatientModel addPatient(PatientModel patientModel) {
        return patientRepository.save(patientModel);
    }

    public List<PatientModel> getPatient() {
        return patientRepository.findAll();
    }

    public boolean existsById(Long id) {
        return patientRepository.existsById(id);
    }

    public void deletePatient(Long id) {
        patientRepository.deleteById(id);
    }
}
