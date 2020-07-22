/*
 * Copyright (C) 2020 Eric Medvet <eric.medvet@gmail.com> (as alikhan4812)
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package it.units.erallab.hmsrobots.core.objects.immutable;

import it.units.erallab.hmsrobots.util.Shape;

public class ControllableVoxel extends Voxel {

  private final double appliedForce;
  private final double controlEnergy;
  private final double controlEnergyDelta;

  public ControllableVoxel(Shape shape, double areaRatio, double appliedForce, double controlEnergy, double controlEnergyDelta) {
    super(shape, areaRatio);
    this.appliedForce = appliedForce;
    this.controlEnergy = controlEnergy;
    this.controlEnergyDelta = controlEnergyDelta;
  }

  public double getAppliedForce() {
    return appliedForce;
  }

  public double getControlEnergy() {
    return controlEnergy;
  }

  public double getControlEnergyDelta() {
    return controlEnergyDelta;
  }
}
