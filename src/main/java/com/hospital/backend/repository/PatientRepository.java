package com.hospital.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.hospital.backend.model.PatientModel;

public interface PatientRepository extends JpaRepository<PatientModel, Long>{
    
}
