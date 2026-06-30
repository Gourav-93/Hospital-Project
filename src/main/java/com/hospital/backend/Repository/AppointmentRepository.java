package com.hospital.backend.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.hospital.backend.Model.AppointmentModel;

public interface AppointmentRepository extends JpaRepository<AppointmentModel, Long> {

}
