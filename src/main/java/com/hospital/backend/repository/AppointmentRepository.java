package com.hospital.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.hospital.backend.model.AppointmentModel;

public interface AppointmentRepository extends JpaRepository<AppointmentModel, Long> {

}
