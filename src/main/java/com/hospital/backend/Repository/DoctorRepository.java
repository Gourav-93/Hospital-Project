package com.hospital.backend.Repository;



import org.springframework.data.jpa.repository.JpaRepository;
import com.hospital.backend.Model.DoctorModel;


public interface DoctorRepository extends JpaRepository<DoctorModel, Long>{
    
}
